import pandas as pd

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df['response_time_log'] = df['response_time'].apply(lambda x: x if x <= 1000 else 1000)
    df['is_peak'] = df['hour'].apply(lambda x: 1 if 12 <= x <= 14 else 0)
    return df
