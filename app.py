from flask import Flask, request, render_template, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib  # For loading the model
import requests  # To make API calls to OpenWeatherMap

# Load the trained model and scaler
model = joblib.load('crop_model.pkl')
scaler = joblib.load('scaler.pkl')

# Create Flask app
app = Flask(__name__)

# Your OpenWeatherMap API key
OPENWEATHER_API_KEY = 'eb1ee8d174d3e16c73fcb7520d79bba7'  # Replace with your actual OpenWeatherMap API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    input_data = request.json

    # Fetch weather data from OpenWeatherMap API
    location = input_data.get('location')
    weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric')
    weather_data = weather_response.json()

    # Check if the weather data was fetched successfully
    if 'main' in weather_data:
        temperature = weather_data['main']['temp']  # Get temperature in Celsius
        humidity = weather_data['main']['humidity']  # Get humidity

        # Prepare input features for prediction
        input_features = [
            input_data['N'],
            input_data['P'],
            input_data['K'],
            input_data['ph'],
            temperature,  # Include temperature
            humidity      # Include humidity
        ]

        # Scale input features
        input_scaled = scaler.transform([input_features])
        
        # Make prediction
        prediction = model.predict(input_scaled)
        
        return jsonify({
            'recommended_crop': prediction[0],
            'temperature': temperature,
            'humidity': humidity
        })
    else:
        return jsonify({'error': 'Could not fetch weather data. Please check the location.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
