from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    features = df[['response_time_log','hour','minute','is_peak']]
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    df['anomaly'] = model.fit_predict(features)
    return df, model
