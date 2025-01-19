import requests
import json

# Define the URL of the Flask API
url = 'http://127.0.0.1:5000/predict'

# Create the input data (same as you would send via curl or Postman)
input_data = {
    "Budget": [100000000],
    "India Net": [20000000],
    "India Gross": [30000000],
    "Overseas": [50000000],
    "Movie Type": [1]  # Make sure this value matches your data encoding
}

# Send a POST request to the Flask API
response = requests.post(url, json=input_data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response (this will contain the prediction)
    predictions = response.json()
    print("Prediction:", predictions)
else:
    print("Failed to get prediction. Status Code:", response.status_code)
