import pandas as pd
import random
import string
import math


def load_csv_to_df(filepath):
    df = pd.read_csv(filepath)
    data = df.values.tolist()
    columns = df.columns.tolist()
    df_data = pd.DataFrame(data, columns=columns)
    return df_data

def _typo(s, max_edits=1):
    s = str(s)
    if not s:
        return s
    chars = list(s)
    for _ in range(max_edits):
        i = random.randrange(len(chars))
        chars[i] = random.choice(string.ascii_letters + string.digits)
    return "".join(chars)

def _corrupt_value(col, val):
    if pd.isna(val):
        return val

    if col == "phonenum":
        try:
            v = int(val)
            delta = random.choice([-9, -5, -2, -1, 1, 2, 5, 9])
            new_v = v + delta

            # ensure non-negative
            if new_v < 0:
                new_v = abs(new_v) + 1  # still "corrupted", but never negative

            return new_v
        except Exception:
            return _typo(val, 1)

    if col == "age":
        try:
            v = int(float(val))  # handles "23" and "23.0"
            delta = random.choice([-7, -5, -2, -1, 1, 2, 5, 7])
            new_age = v + delta

            # ensure numeric + non-negative (optional clamp upper bound if you want)
            new_age = max(0, new_age)
            return int(new_age)
        except Exception:
            # if age is non-numeric, keep it numeric by generating a nearby numeric value
            # (fallback: try casting from extracted digits could be added if needed)
            return random.randint(0, 99)

    if col == "postcode":
        return _typo(val, 1)

    if col == "emailid":
        v = str(val)
        if len(v) > 2 and random.random() < 0.5:
            return v[:-1]
        return v + random.choice(["1", ".", "_x", "00"])

    if col == "sname":
        return _typo(val, 1)

    if col == "address":
        v = str(val)
        return v + f" Apt {random.randint(1, 99)}"

    return _typo(val, 1)




def generate_corruptions_for_student_data(
    truth_df: pd.DataFrame,
    LHS,
    RHS,
    n_versions: int = 20,
    target_violation_frac: float | None = None,
    clusters_per_version=(2, 5),
    dups_per_cluster=(2, 6),
    cells_corrupted=(2, 5),
    force_diff_rhs: bool = True,
    seed: int = 42,
    shuffle: bool = True,
):
    for c in LHS + RHS:
        if c not in truth_df.columns:
            raise ValueError(f"Missing column '{c}' in truth_df")

    keys = truth_df[LHS].drop_duplicates().values.tolist()
    n_keys = len(keys)
    if n_keys == 0:
        raise ValueError("truth_df has no rows/keys to corrupt")

    dirty_versions = []

    for i in range(n_versions):
        random.seed(seed + i)
        df_dirty = truth_df.copy()
        if target_violation_frac is not None:
            if not (0.0 <= target_violation_frac <= 1.0):
                raise ValueError("target_violation_frac must be between 0 and 1")
            m = max(1, min(n_keys, math.ceil(target_violation_frac * n_keys)))
        else:
            m = random.randint(clusters_per_version[0], min(clusters_per_version[1], n_keys))

        chosen_keys = random.sample(keys, m)

        for sid_val, uni_val in chosen_keys:
            base_row = truth_df[(truth_df["sid"] == sid_val) & (truth_df["university"] == uni_val)].iloc[0]
            k = random.randint(dups_per_cluster[0], dups_per_cluster[1])
            for _ in range(k):
                new_row = base_row.copy()

                c = random.randint(cells_corrupted[0], min(cells_corrupted[1], len(RHS)))
                cols = random.sample(RHS, c)

                changed_any = False
                for col in cols:
                    old = new_row[col]
                    new = _corrupt_value(col, old)
                    if new != old:
                        changed_any = True
                    new_row[col] = new

                # guarantee a conflict
                if force_diff_rhs and not changed_any:
                    col = random.choice(RHS)
                    new_row[col] = _corrupt_value(col, new_row[col])

                df_dirty = pd.concat([df_dirty, pd.DataFrame([new_row])], ignore_index=True)

        if shuffle:
            df_dirty = df_dirty.sample(frac=1, random_state=seed + i).reset_index(drop=True)

        dirty_versions.append(df_dirty)

    return dirty_versions