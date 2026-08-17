def get_summary_stats(df):
    mean = df.mean(numeric_only=True)
    std = df.std(numeric_only=True)
    print(f"mean: {mean}, std: {std}")
    return mean, std
