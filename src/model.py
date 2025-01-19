import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def train_model(X_train, X_test, y_train, y_test):
    # Set the experiment name and tracking URI (for local setup)
    mlflow.set_tracking_uri("http://localhost:5000")  # Set the correct tracking URI
    mlflow.set_experiment("Movie Box Office Prediction")
    
    # Initialize the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Start MLflow run
    mlflow.start_run()
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Mean Absolute Error: {mae}")
    
    # Log parameters, metrics, and the model
    mlflow.log_param('n_estimators', 100)
    mlflow.log_metric('mae', mae)
    mlflow.sklearn.log_model(model, 'random_forest_model')
    
    # End MLflow run
    mlflow.end_run()
    
    return model, mae
