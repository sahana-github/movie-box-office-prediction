from setuptools import setup, find_packages

setup(
    name="movie-box-office-prediction",
    version="0.1.0",
    description="A project for predicting box office collections using MLOps tools.",
    author="Sahana Durgekar",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "dvc",
        "mlflow",
        "airflow",
    ],
    entry_points={
        "console_scripts": [
            "run-pipeline=pipelines.pipeline:run_pipeline",
        ],
    },
    python_requires=">=3.7",
)
