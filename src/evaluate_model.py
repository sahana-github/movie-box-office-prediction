import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from data_processing import preprocess_data  # Ensure you import the preprocess_data function

def evaluate_model(model, X_test, y_test):
    # Predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Log metrics in MLflow
    mlflow.log_metric('mae', mae)
    mlflow.log_metric('mse', mse)
    mlflow.log_metric('r2', r2)
    
    print(f"Model Evaluation:\n MAE: {mae}\n MSE: {mse}\n R2: {r2}")
    
    return mae, mse, r2

# Get the processed data
X_train, X_test, y_train, y_test = preprocess_data()

# Load the trained model from MLflow
model_uri = "runs:/7d0ac33ff3834ab0b19e66c5d6d4f39e/random_forest_model"  # Replace with your actual run ID
model = mlflow.sklearn.load_model(model_uri)

# Call evaluate_model
evaluate_model(model, X_test, y_test)
