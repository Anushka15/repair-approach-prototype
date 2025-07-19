import re
def extract_attribute(rv):
    match = re.match(r'fd\d+([A-Za-z]+)\d+=\d+', rv)
    return match.group(1) if match else None


def create_repaired_rows(rv_definitions, df_data, consistent_rows):
    repaired_rows = []
    row_index_map = {}
    uuid_to_row = df_data.set_index('uuid').to_dict('index')

    # Step 1: Process repaired rows with RVs
    for rv, (rhs_value, uuid_set) in rv_definitions.items():
        rhs_col = extract_attribute(rv)  # e.g., 'B' from 'fd1_B1=1'
        for uid in uuid_set:
            row_key = (uid, rhs_value)

            if row_key not in row_index_map:
                base_row = uuid_to_row[uid].copy()
                base_row[rhs_col] = rhs_value

                # Exclude 'uuid' column
                row_values = [base_row[col] for col in df_data.columns if col != 'uuid']

                # Start a new sentence list
                repaired_rows.append(row_values + [[rv]])
                row_index_map[row_key] = len(repaired_rows) - 1
            else:
                idx = row_index_map[row_key]
                repaired_rows[idx][-1].append(rv)

    # Step 2: Convert sentence list to a Bdd('...') string
    for row in repaired_rows:
        sentence_list = row.pop()
        bdd_expr = ' | '.join(sentence_list)
        row.append(bdd_expr)

    # Step 3: Append consistent rows with Bdd('1')
    for uid in consistent_rows:
        row_data = df_data[df_data['uuid'] == uid]

        if not row_data.empty:
            # Drop 'uuid' and convert to list
            row_values = row_data.drop(columns='uuid').values.tolist()[0]
            row_values.append(1)
            repaired_rows.append(row_values)

    return repaired_rows