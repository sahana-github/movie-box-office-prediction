from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from src.model import train_model
from sklearn.model_selection import train_test_split
import pandas as pd

# Load your dataset here (update the path to your dataset)
data = pd.read_csv("data/processed/processed_movies.csv")
X = data.drop("Worldwide", axis=1)  # Replace 'target_column' with your target variable name
y = data["Worldwide"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# List of models to train
model_names = ["random_forest", "gradient_boosting", "linear_regression", "decision_tree"]

def train_model_task(model_name):
    train_model(X_train, X_test, y_train, y_test, model_name)

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'model_training_pipeline',
    default_args=default_args,
    description='Train multiple models for box office prediction',
    schedule_interval=None,  # Trigger manually
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    # Create tasks dynamically for each model
    for model_name in model_names:
        PythonOperator(
            task_id=f'train_{model_name}',
            python_callable=train_model_task,
            op_args=[model_name],
        )
