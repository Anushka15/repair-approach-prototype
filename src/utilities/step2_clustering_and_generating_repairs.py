import math
from itertools import product,combinations
from collections import defaultdict
import pandas as pd
from pandas.api.types import is_integer_dtype, is_float_dtype

MAX_VARNAME_LEN = 11


def preprocess_data(df_data):
    #df_data['uuid'] = [uuid.uuid4() for _ in range(len(df_data))]
    #cleaned_df = df_data.drop_duplicates().reset_index(drop=True)
    df_data['uuid'] = range(1, len(df_data) + 1)
    return df_data

def identify_clusters(table_df, fd_lhs):
    cleaned_df = table_df.drop_duplicates().reset_index(drop=True)
    groups = cleaned_df.groupby(fd_lhs)
    return groups

def find_minimum_actions(cluster,fd_rhs):
    kmax = cluster[fd_rhs].value_counts().iloc[0]
    num_rows = len(cluster)
    min_actions = num_rows - kmax
    return min_actions,num_rows,kmax

def mark_high_frequence_subclusters(cluster,fd_rhs,kmax):
    subclusters = cluster.groupby(fd_rhs)
    group_sizes = subclusters.size()
    fd_rhs_values_with_kmax = group_sizes[group_sizes == kmax].index
    filtered_rows = cluster[cluster[fd_rhs].isin(fd_rhs_values_with_kmax)]
    uuid_dict = filtered_rows.groupby(fd_rhs)['uuid'].apply(list).to_dict()
    return uuid_dict


def create_rv_definitions(df_data,fd_constraint):
    rv_definitions = {}
    rv_probabilities = {}
    consistent_rows = []
    for fd_id, (lhs, [rhs]) in enumerate(fd_constraint, 1):
        clusters = identify_clusters(df_data, lhs)
        for cluster_id, (cluster_key, cluster) in enumerate(clusters, 1):
            min_actions,num_rows,kmax = find_minimum_actions(cluster,rhs)
            if min_actions == 0:
                consistent_rows.extend(cluster['uuid'].tolist())
                continue
            uuid_dict = mark_high_frequence_subclusters(cluster,rhs,kmax)
            all_uuids = cluster['uuid']
            rv_index = 1
            for fd_rhs_value, uuid_list in uuid_dict.items():
                rhs_value = cluster.loc[cluster['uuid'] == uuid_list[0], rhs].iloc[0]
                base_set = set(uuid_list)
                remaining = list(set(all_uuids) - base_set)
                for i in range(min_actions + 1):
                    for combo in combinations(remaining, i):
                        extended_set = base_set.union(combo)
                        rv = f"fd{fd_id}{rhs}{cluster_id}={rv_index}"
                        rv_definitions[rv] = (rhs_value,extended_set)
                        rv_probabilities[rv] = 1.0
                        rv_index+=1
            for rv_def in rv_probabilities:
                if rv_def.split("=")[0] == rv.split("=")[0]:
                    rv_probabilities[rv_def] = 1 / (rv_index-1)
    return rv_definitions,rv_probabilities,consistent_rows


def compute_scores_for_rvs(prob_type, cost, eps=1e-9):
    if prob_type == 'UNIFORM':
        score = 1.0
    elif prob_type == 'COST_BASED':
        if cost == 0:
            score = 1.0 / eps
        else:
            score = 1.0 / (cost + eps)
    else:
        raise ValueError(f"Unknown prob_type: {prob_type}")

    return score


def compute_actions(df_data, fd_constraints, constraint_hardness, delete_cost=1, update_cost=1, eps=1e-9,
                    prob_type='uniform'):
    actions_list = []
    rv_probs = {}

    if not fd_constraints:
        return actions_list, []

    common_lhs = fd_constraints[0][0]
    clusters = list(identify_clusters(df_data, common_lhs))
    cluster_ids = list(range(1, len(clusters) + 1))
    for fd_id, (lhs, [rhs]) in enumerate(fd_constraints, start=1):
        fd_repairs = []
        fd_rv_scores = {}
        total_score = 0.0
        for cluster_id, (cluster_key, cluster) in enumerate(clusters, start=1):

            min_actions, num_rows, kmax = find_minimum_actions(cluster, rhs)
            all_uuids = cluster['uuid'].tolist()
            all_uuid_set = set(all_uuids)
            uuid_to_rhs = dict(zip(all_uuids, cluster[rhs].tolist()))
            if min_actions == 0:
                continue
            rv_counter = 1

            for uuid in all_uuids:
                correct_value = uuid_to_rhs[uuid]
                base_set = {uuid}
                remaining = list(all_uuid_set - base_set)

                for i in range(num_rows + 1):
                    for combo in combinations(remaining, i):
                        extended_set = base_set.union(combo)
                        dr = list(all_uuid_set - extended_set)
                        ur = [
                            upd_uuid
                            for upd_uuid in extended_set
                            if uuid_to_rhs[upd_uuid] != correct_value
                        ]

                        cost = (len(dr) * delete_cost) + (len(ur) * update_cost)

                        varname = f"fd{fd_id}{rhs}{cluster_id}"
                        if len(varname) > MAX_VARNAME_LEN:
                            varname = varname[:MAX_VARNAME_LEN]

                        rv = f"{varname}={rv_counter}"

                        #rv = f"fd{fd_id}{rhs}{cluster_id}={rv_counter}"
                        row_def = {
                            'FD': fd_id,
                            'LHS': lhs,
                            'Cluster': cluster_id,
                            'Tuples': extended_set,
                            'TargetValue': correct_value,
                            'DR': dr,
                            'UR': [f"{r}:{rhs}={correct_value}" for r in ur],
                            'Cost': cost,
                            'min_cost': min_actions,
                            'rv': rv
                        }
                        score = compute_scores_for_rvs(prob_type, cost, eps) * constraint_hardness[fd_id - 1]
                        fd_rv_scores[rv] = score
                        total_score += score
                        rv_counter += 1
                        fd_repairs.append(row_def)

        fd_rv_probs = {}
        for fd_rv in fd_rv_scores:
            fd_rv_probs[fd_rv] = fd_rv_scores[fd_rv] / total_score
        rv_probs.update(fd_rv_probs)
        actions_list.append(fd_repairs)

    return actions_list, cluster_ids, rv_probs



def parse_tuple_id(ur_str):
    return ur_str.split(':', 1)[0]


def combine_fd_repairs_for_cluster(fd_actions, cluster_id,delete_cost,update_cost):
    fd_info = []
    for per_fd_repairs in fd_actions:
        cand = [r for r in per_fd_repairs if r['Cluster'] == cluster_id]
        if not cand:
            continue

        fd_id = cand[0]['FD']
        min_cost_fd = min(r['Cost'] for r in cand)
        fd_info.append((fd_id, min_cost_fd, cand))

    if not fd_info:
        return [],0

    fd_ids = [fd_id for (fd_id, _, _) in fd_info]
    min_cost_sum = sum(min_cost_fd for (_, min_cost_fd, _) in fd_info)

    combined_repairs = []
    repair_lists = [cand for (_, _, cand) in fd_info]

    seen = set()

    for combo in product(*repair_lists):
        conflict = False
        combined_dr_ids = set()
        combined_ur_ids = set()
        combined_ur_strings = set()
        rv_parts = []
        combined_tuple_ids = set()

        for r in combo:

            rv = r.get('rv')
            if rv:
                rv_parts.append(rv)

            combined_tuple_ids |= {str(tid) for tid in r['Tuples']}

            dr_ids = {str(tid) for tid in r['DR']}

            ur_ids = set()
            for ur in r['UR']:
                tid = parse_tuple_id(ur)
                ur_ids.add(tid)
                combined_ur_strings.add(ur)

            if dr_ids & combined_ur_ids:
                conflict = True
                break
            if ur_ids & combined_dr_ids:
                conflict = True
                break

            combined_dr_ids |= dr_ids
            combined_ur_ids |= ur_ids

            if len(combined_dr_ids | combined_ur_ids) > min_cost_sum:
                conflict = True
                break

        if conflict:
            continue

        num_deleted = len(combined_dr_ids)
        num_updated = len(combined_ur_ids)

        combined_cost = delete_cost * num_deleted + update_cost * num_updated

        if combined_cost > min_cost_sum:
            continue

        sentence = " & ".join(rv_parts)
        key = (
            tuple(sorted(combined_dr_ids)),
            tuple(sorted(combined_ur_strings)),
            sentence,
        )
        if key in seen:
            continue
        seen.add(key)

        combined_repairs.append({
            'Cluster': cluster_id,
            'DR': sorted(combined_dr_ids),
            'UR': sorted(combined_ur_strings),
            'Tuples': sorted(combined_tuple_ids),
            'Cost': combined_cost,
            'sentence': sentence
        })
    return combined_repairs, math.prod(len(lst) for lst in repair_lists)


def min_cost_actions(cluster_ids,actions,delete_cost,update_cost):
    combined_actions = []
    total_repair = 0
    for cluster_id in cluster_ids:
        combined,num_repairs = combine_fd_repairs_for_cluster(actions, cluster_id,delete_cost,update_cost)
        total_repair += num_repairs
        if combined:
            min_cost = min(r['Cost'] for r in combined)
            combined_actions.append([r for r in combined if r['Cost'] == min_cost])
    all_actions = [item for sublist in combined_actions for item in sublist]
    return all_actions,total_repair/len(cluster_ids)




def cast_column_dtype(val_str, col_series):
    if is_integer_dtype(col_series.dtype):
        return int(val_str)
    if is_float_dtype(col_series.dtype):
        return float(val_str)
    return val_str


def apply_combined_actions(df, combined_action_list, uuid_col="uuid"):
    repaired_dfs = []
    all_tuple_ids = set()
    for action_idx, action in enumerate(combined_action_list, start=1):
        tuple_ids = [str(tid) for tid in action.get("Tuples", [])]
        all_tuple_ids.update(tuple_ids)
        df_rep = df[df[uuid_col].astype(str).isin(tuple_ids)].copy()
        for ur in action.get("UR", []):
            tup_part, assign_part = ur.split(":", 1)
            attr, val_str = assign_part.split("=", 1)

            tup_id = int(tup_part)
            val = cast_column_dtype(val_str, df_rep[attr])
            df_rep.loc[df_rep[uuid_col] == tup_id, attr] = val
        df_rep["_sentences"] = action.get("sentence", "")

        repaired_dfs.append(df_rep)

    clean = df[~df[uuid_col].astype(str).isin(all_tuple_ids)].copy()
    clean["_sentences"] = 1
    repaired_dfs.append(clean)
    return repaired_dfs




def condition_probability_for_used_rvs(rv_probs):
    groups = defaultdict(list)
    for rv, p in rv_probs.items():
        var = rv.split('=')[0]
        groups[var].append(rv)

    for var, keys in groups.items():
        group_sum = sum(rv_probs[k] for k in keys)
        if group_sum > 0:
            for k in keys:
                rv_probs[k] = round((rv_probs[k] / group_sum),4)
        else:
            n = len(keys)
            for k in keys:
                rv_probs[k] = round((1.0 / n),4)

    return rv_probs

def filter_and_condition_min_cost_rvs(rv_probs,
                                              repaired_df,
                                              sentence_col="_sentences",
                                              sep="&"):

    used_rvs = set()
    if sentence_col in repaired_df.columns:
        for s in repaired_df[sentence_col].dropna():
            s = str(s)
            tokens = s.split(sep)
            for tok in tokens:
                rv = tok.strip()
                if rv:
                    used_rvs.add(rv)
    for rv in list(rv_probs.keys()):
        if rv not in used_rvs:
            del rv_probs[rv]
    return condition_probability_for_used_rvs(rv_probs)
