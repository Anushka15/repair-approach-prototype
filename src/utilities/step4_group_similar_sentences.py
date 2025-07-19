def group_similar_rows_together(repaired_df):
    group_cols = [col for col in repaired_df.columns if col != '_sentences']

    def format_sentences(s):
        unique_sentences = list(map(str, s.unique()))
        if len(unique_sentences) == 1:
            return unique_sentences[0]
        return ' | '.join(f"({sentence})" for sentence in unique_sentences)

    merged_df = (
        repaired_df
        .groupby(group_cols, as_index=False)
        .agg({'_sentences': format_sentences})
    )
    return merged_df