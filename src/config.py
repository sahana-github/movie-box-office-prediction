# src/config.py
import os

# src/config.py

# File paths
RAW_DATA_PATH = os.path.join("data", "raw", "bollywood_2022.csv")
PROCESSED_DATA_PATH = os.path.join("data", "processed", "bollywood_movies_processed.csv")

# MLflow experiment name
MLFLOW_EXPERIMENT_NAME = "Movie Box Office Prediction"

# Model hyperparameters
MODEL_PARAMS = {
    'n_estimators': 100,
    'max_depth': 10,
}

# File paths
DATA_PATH = 'data/processed/bollywood_movies_processed.csv'
LOG_FILE = 'movie_prediction.log'
