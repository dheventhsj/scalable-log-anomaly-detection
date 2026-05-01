import pandas as pd
import pickle
from sklearn.ensemble import IsolationForest
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    df["minute"] = df["timestamp"].dt.minute
    return df


def build_pipeline():
    return Pipeline([
        ("scaler", StandardScaler()),
        ("model", IsolationForest(
            n_estimators=200,
            contamination=0.05,
            random_state=42,
            n_jobs=-1
        ))
    ])


def run_pipeline():
    df = load_data("data/logs.csv")

    # Feature matrix (vectorized)
    X = df[["response_time", "hour", "minute"]]

    pipeline = build_pipeline()
    preds = pipeline.fit_predict(X)

    df["anomaly"] = preds

    # Save outputs
    df.to_csv("data/output.csv", index=False)

    with open("models/pipeline.pkl", "wb") as f:
        pickle.dump(pipeline, f)

    print("✅ Efficient pipeline completed")
