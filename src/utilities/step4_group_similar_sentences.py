import re
from collections import OrderedDict

import pandas as pd

def group_similar_rows_together(repaired_df, join_op=" | "):

    group_cols = [col for col in repaired_df.columns if col != '_sentences']

    def combine_sentences(series):
        seen = set()
        ordered = []
        for cell in series:
            if pd.isna(cell):
                continue
            s = str(cell)
            if s not in seen:
                seen.add(s)
                ordered.append(s)

        if not ordered:
            return ""

        return join_op.join(f"({s})" for s in ordered)

    merged_df = (
        repaired_df
        .groupby(group_cols, as_index=False)
        .agg({'_sentences': combine_sentences})
    )

    return merged_df
