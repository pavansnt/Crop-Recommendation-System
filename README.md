# 🌱 AI-Powered Crop Recommendation System

A comprehensive web application that provides intelligent crop recommendations based on soil parameters and real-time weather data using machine learning.

## 📋 Project Overview

This Crop Recommendation System helps farmers and agricultural professionals make informed decisions about crop cultivation by analyzing soil nutrients (Nitrogen, Phosphorus, Potassium, pH levels) and integrating real-time weather data from the OpenWeatherMap API.

## ✨ Features

- **🤖 Machine Learning Powered**: Uses Random Forest Classifier for accurate crop predictions
- **🌤️ Real-time Weather Integration**: Fetches current weather data based on location
- **🌐 Bilingual Interface**: Supports both English and Kannada languages
- **📊 Soil Analysis**: Considers N, P, K, and pH levels for recommendations
- **🎯 User-friendly Web Interface**: Responsive design with intuitive form inputs
- **⚡ Fast Predictions**: Real-time recommendations with detailed weather insights

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn, Random Forest Classifier
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Processing**: Pandas, NumPy
- **API Integration**: OpenWeatherMap API
- **Model Persistence**: Joblib

## 📁 Project Structure

```
.
├── app.py                 # Flask application
├── train_model.py         # Machine learning model training script
├── crop_model.pkl         # Trained Random Forest model
├── scaler.pkl            # Feature scaler
├── crop_data.csv         # Dataset for training
├── requirements.txt      # Python dependencies
├── linkedin_post.md      # Project documentation
└── templates/
    ├── index.html        # Main web interface
    └── static/
        └── style.css     # CSS styles
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd Project
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up OpenWeatherMap API
1. Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your API key
3. Replace the API key in `app.py`:
```python
OPENWEATHER_API_KEY = 'your_actual_api_key_here'
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## 📊 Usage

1. **Enter Location**: Input your geographical location (city name)
2. **Soil Parameters**: Provide values for:
   - Nitrogen (N) levels
   - Phosphorus (P) levels  
   - Potassium (K) levels
   - pH level
3. **Get Recommendation**: Click "Get Recommendation" to receive crop suggestions
4. **View Results**: See the recommended crop along with current weather data

## 🧠 Machine Learning Model

### Training Data
The model is trained on agricultural dataset containing:
- Soil nutrient levels (N, P, K, pH)
- Environmental factors (temperature, humidity)
- Crop labels for various agricultural products

### Model Details
- **Algorithm**: Random Forest Classifier
- **Features**: N, P, K, pH, temperature, humidity
- **Training**: 80% training, 20% testing split
- **Accuracy**: High prediction accuracy (specific metrics available after training)

### Retraining the Model
To retrain the model with new data:
```bash
python train_model.py
```

## 🌐 API Endpoints

### POST /recommend
Returns crop recommendation based on input parameters.

**Request Body:**
```json
{
  "location": "Bangalore",
  "N": 90,
  "P": 42,
  "K": 43,
  "ph": 6.5
}
```

**Response:**
```json
{
  "recommended_crop": "rice",
  "temperature": 28.5,
  "humidity": 65,
  "weather_description": "clear sky"
}
```

## 🔧 Configuration

### Environment Variables
- `OPENWEATHER_API_KEY`: Your OpenWeatherMap API key
- `FLASK_ENV`: Set to 'development' for debug mode

### Model Configuration
- Model file: `crop_model.pkl`
- Scaler file: `scaler.pkl`
- Training data: `crop_data.csv`

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenWeatherMap for providing weather data API
- Scikit-learn team for machine learning libraries
- Flask community for the web framework
- Agricultural research institutions for dataset contributions


## 🎯 Future Enhancements

- [ ] Mobile app development
- [ ] Additional language support
- [ ] Historical weather data integration
- [ ] Soil moisture sensor integration
- [ ] Yield prediction features
- [ ] Pest and disease detection
- [ ] Market price trends

---

**Note**: This is a 4th semester mini project developed for educational purposes. Always consult with agricultural experts for critical farming decisions.
