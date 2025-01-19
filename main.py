from src.data_processing import preprocess_data
from src.model import train_model
from src.utils import setup_logger

# Set up logger
logger = setup_logger()

# Preprocess the data
X_train, X_test, y_train, y_test = preprocess_data()

# Train the model and log results
model, mae = train_model(X_train, X_test, y_train, y_test)

# Log final output
logger.info(f"Model trained with MAE: {mae}")
