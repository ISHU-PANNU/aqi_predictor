from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model and scaler
with open('air_quality_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input features from the form
        CO_GT = float(request.form['CO(GT)'])
        C6H6_GT = float(request.form['C6H6(GT)'])
        T = float(request.form['T'])
        RH = float(request.form['RH'])
        NOx_GT = float(request.form['NOx(GT)'])

        # Create the feature array for prediction
        features = np.array([[CO_GT, C6H6_GT, T, RH, NOx_GT]])

        # Scale the features using the same scaler used during training
        scaled_features = scaler.transform(features)

        # Predict the AQI
        predicted_AQI = model.predict(scaled_features)[0]

        # Return the predicted AQI as a JSON response
        return jsonify({'predicted_AQI': predicted_AQI})

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': 'Error in prediction'})

if __name__ == '__main__':
    app.run(debug=True)












