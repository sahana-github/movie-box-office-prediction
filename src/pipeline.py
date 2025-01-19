# src/pipeline.py

from src.data_processing import preprocess_data
from src.model import train_model

def pipeline(data_path):
    # Step 1: Data Processing
    X_train, X_test, y_train, y_test = preprocess_data(data_path)

    # Step 2: Model Training
    model, mae = train_model(X_train, X_test, y_train, y_test)
    
    print(f"Model MAE: {mae}")
    return model

if __name__ == "__main__":
    pipeline('data/processed/processed_movies.csv')
