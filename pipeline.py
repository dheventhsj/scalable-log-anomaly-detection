from src.log_parser import parse_logs
from src.feature_engineering import create_features
from src.anomaly import detect_anomalies
import pickle

def run_pipeline():
    df = parse_logs("data/logs.csv")
    df = create_features(df)
    df, model = detect_anomalies(df)

    df.to_csv("data/output.csv", index=False)

    with open("models/model.pkl","wb") as f:
        pickle.dump(model,f)

    print("Pipeline completed and model saved.")
