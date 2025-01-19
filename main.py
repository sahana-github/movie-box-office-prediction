from src.data_processing import preprocess_data
from src.model import train_model
from src.utils import setup_logger

# Set up logger
logger = setup_logger()

# Preprocess the data
X_train, X_test, y_train, y_test = preprocess_data()

# Define the list of models you want to test (you can dynamically get them from the train_model function)
model_names = ["random_forest", "gradient_boosting", "linear_regression", "decision_tree"]

# Iterate over all models
for model_name in model_names:
    # Train the model and log results
    model, mae = train_model(X_train, X_test, y_train, y_test, model_name)

    # Log final output for each model
    logger.info(f"Model: {model_name} trained with MAE: {mae}")
