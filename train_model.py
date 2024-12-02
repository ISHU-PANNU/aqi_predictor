import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle

# Load the dataset
file_path = 'air_quality_data.csv'
data = pd.read_csv(file_path)

# Check if the dataset is loaded correctly
print(data.head())

# Define the feature columns and the target column
X = data[['CO(GT)', 'C6H6(GT)', 'T', 'RH', 'NOx(GT)']]  # Feature columns
y = data['AQI']  # Target column

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Save the trained model and scaler to disk
with open('air_quality_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

print("Model and scaler have been saved.")






