Here's a beginner-friendly README for your project:

# Movie Box Office Prediction with MLOps

![image](https://github.com/user-attachments/assets/5db471ce-091e-48c4-a0ed-9544c65826a5)


This project predicts movie box office collections using machine learning models. The project includes features like training models, evaluating them, and logging the results using **MLflow**. It also demonstrates how to structure an MLOps pipeline with version control and continuous integration/continuous deployment (CI/CD) practices.

## Requirements

Before you start, make sure you have the following installed:

1. **Python 3.8 or later** (Recommended: 3.9)
2. **MLflow** - For model tracking and logging.
3. **Scikit-Learn** - For machine learning models.
4. **Airflow** (optional, for workflow automation)
5. **DVC** (Data Version Control) (optional, for dataset versioning)
6. **Docker** (optional, for containerization)

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Project Structure

```
movie-box-office-prediction/
├── main.py                  # Main file for training models
├── src/
│   ├── data_processing.py   # Data cleaning and preprocessing
│   ├── model.py             # Model training and evaluation
│   └── utils.py             # Utility functions (e.g., logging setup)
├── data/                    # Raw and processed datasets
└── logs/                    # Logs for model training and evaluation
```

## Steps to Run

1. **Prepare Data**: Place your dataset (`processed_movies.csv`) in the `data/` folder.

2. **Preprocess Data**: Use the `data_processing.py` script to clean and preprocess your data.

3. **Train Models**: Run the `main.py` script to train different machine learning models and log results to **MLflow**.

    ```bash
    python main.py
    ```

4. **MLflow UI**: To track experiments, start the **MLflow UI** by running:

    ```bash
    mlflow ui
    ```

    Visit `http://localhost:5000` in your browser to view the MLflow dashboard.

## Models Included

- Random Forest Regressor
- Gradient Boosting Regressor
- Linear Regression
- Decision Tree Regressor

The models are trained using the data, and their performance is evaluated using the **Mean Absolute Error (MAE)**.

## Optional: Running with Airflow

If you want to automate the workflow, you can use **Apache Airflow** to schedule and monitor the model training pipeline.

Install Airflow with:

```bash
pip install apache-airflow
```

Start the Airflow webserver:

```bash
airflow webserver
```

And run the tasks using:

```bash
airflow scheduler
```

## CI/CD (Optional)

You can set up **CI/CD pipelines** for automated testing and deployment of models using services like GitHub Actions, Jenkins, or GitLab CI.

## Troubleshooting

If you encounter issues with `pip install` or Airflow, check that you have all system dependencies installed (e.g., build tools and libraries).
