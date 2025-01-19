from flask import Flask, request, jsonify
import mlflow
import mlflow.sklearn
import pandas as pd

app = Flask(__name__)

# Load the model at the start of the app (to avoid loading it on every request)
model_uri = "runs:/7d0ac33ff3834ab0b19e66c5d6d4f39e/random_forest_model"  # Replace <run_id> with your actual run ID
model = mlflow.sklearn.load_model(model_uri)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json(force=True)
    
    # Convert JSON to DataFrame
    input_data = pd.DataFrame(data)
    
    # Make predictions
    predictions = model.predict(input_data)
    
    # Return predictions as JSON
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)
