from itertools import product,combinations
def preprocess_data(df_data):
    #df_data['uuid'] = [uuid.uuid4() for _ in range(len(df_data))]
    cleaned_df = df_data.drop_duplicates().reset_index(drop=True)
    cleaned_df['uuid'] = range(1, len(cleaned_df) + 1)
    return cleaned_df

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