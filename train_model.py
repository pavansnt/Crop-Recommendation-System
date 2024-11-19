import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

# Load your existing dataset with tab as the delimiter
data = pd.read_csv('crop_data.csv', sep='\t')  # Update with your actual dataset file

# Print columns to check what is available
print("Columns in the dataset:", data.columns)

# Prepare features and target variable
try:
    # Adjust these column names based on what you see in the print statement
    X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph']]  # Include temperature and humidity
    y = data['label']  # Assuming 'label' is the target variable

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train the Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Save the trained model and the scaler
    joblib.dump(model, 'crop_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')

    # Optionally, evaluate your model
    accuracy = model.score(X_test_scaled, y_test)
    print(f'Model accuracy: {accuracy * 100:.2f}%')

except KeyError as e:
    print(f"KeyError: One or more columns are missing in the dataset. Please check the following column names: {e}")