# Advanced Distributed Log Analyzer with Anomaly Detection

## Overview
This project simulates a production-style log monitoring system with anomaly detection.

## Features
- Log parsing with timestamps
- Feature engineering
- Isolation Forest anomaly detection
- Model persistence
- REST API for querying logs and anomalies

## Run
pip install -r requirements.txt
python run.py
uvicorn app.main:app --reload

## Endpoints
- /logs
- /anomalies
