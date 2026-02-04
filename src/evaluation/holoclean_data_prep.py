import pandas as pd

def create_truth_for_holoclean(input_file_path,output_file_path):
    df = pd.read_csv(input_file_path)
    df.insert(0, "tid", range(len(df)))
    long_df = df.melt(
        id_vars="tid",
        var_name="attribute",
        value_name="correct_val"
    )

    col_order = [c for c in df.columns if c != "tid"]
    long_df["attribute"] = pd.Categorical(long_df["attribute"], categories=col_order, ordered=True)
    long_df = long_df.sort_values(["tid", "attribute"]).reset_index(drop=True)
    print(long_df.head(5))
    long_df.to_csv(output_file_path, index=False)


def fd_constraints_to_dc_strings(fd_constraints):
    dc_lines = []

    for lhs, rhs_list in fd_constraints:
        base_parts = ["t1", "t2"] + [f"EQ(t1.{a},t2.{a})" for a in lhs]
        for rhs in rhs_list:
            dc = "&".join(base_parts + [f"IQ(t1.{rhs},t2.{rhs})"])
            dc_lines.append(dc)

    return dc_lines


def write_denial_constraints_txt(fd_constraints, output_txt_path):
    dc_lines = fd_constraints_to_dc_strings(fd_constraints)
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(dc_lines))
    return output_txt_path


def read_truth_csv_holoclean(input_file_name):

    df_long = pd.read_csv(input_file_name, keep_default_na=False)
    attr_order = df_long.drop_duplicates("attribute")["attribute"].tolist()
    df_long = (df_long
               .sort_values(["tid"])  # optional
               .drop_duplicates(subset=["tid", "attribute"], keep="first"))
    df_wide = (df_long
               .pivot(index="tid", columns="attribute", values="correct_val")
               .reset_index())
    df_wide = df_wide[["tid"] + [a for a in attr_order if a in df_wide.columns]]
    df_wide = df_wide.rename_axis(None, axis=1)
    return df_wide




