import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# Define available models
models = {
    "random_forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "gradient_boosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
    "linear_regression": LinearRegression(),
    "decision_tree": DecisionTreeRegressor(random_state=42),
}

def train_model(X_train, X_test, y_train, y_test, model_name):
    # Check if the model is available
    if model_name not in models:
        raise ValueError(f"Model {model_name} not found. Available models: {list(models.keys())}")

    # Set MLflow Tracking URI and Experiment Name
    tracking_uri = "http://localhost:5000"  # Set your MLflow tracking server URI
    experiment_name = "Movie Box Office Prediction"
    
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)

    model = models[model_name]  # Initialize the selected model

    # Start MLflow run
    with mlflow.start_run(run_name=model_name):  # Use the model name for run_name
        # Train the model
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate the model
        mae = mean_absolute_error(y_test, y_pred)
        print(f"Model: {model_name}, Mean Absolute Error: {mae}")

        # Log parameters, metrics, and the model
        mlflow.log_param('model_name', model_name)
        if hasattr(model, 'n_estimators'):
            mlflow.log_param('n_estimators', model.n_estimators)
        mlflow.log_metric('mae', mae)
        mlflow.sklearn.log_model(model, f'{model_name}_model')

    return model, mae
