# src/data_processing.py

import pandas as pd
import os
from sklearn.model_selection import train_test_split

def preprocess_data():
    # Define the raw data path
    raw_data_path = os.path.join("data", "raw", "bollywood_2022.csv")
    
    # Load the raw data
    data = pd.read_csv(raw_data_path)
    
    # Handle missing values (drop rows with any missing values)
    data = data.dropna()

    # Feature engineering
    # Encoding 'Movie Type' as categorical codes
    data['Movie Type'] = data['Movie Type'].astype('category').cat.codes  
    
    # Adjust features (this can change based on the columns in your data)
    X = data[['Budget', 'India Net', 'India Gross', 'Overseas', 'Movie Type']]
    y = data['Worldwide']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Save the processed data for later use
    processed_data_path = os.path.join("data", "processed", "bollywood_movies_processed.csv")
    data.to_csv(processed_data_path, index=False)
    
    # Save the split data
    return X_train, X_test, y_train, y_test
