import pandas as pd
import numpy as np

# Number of rows for dataset
num_rows = 1000

# Generate synthetic data for required columns
data = {
    'CO(GT)': np.random.uniform(0, 10, num_rows),
    'C6H6(GT)': np.random.uniform(0, 10, num_rows),
    'T': np.random.uniform(20, 35, num_rows),  # Temperature in °C
    'RH': np.random.uniform(30, 70, num_rows),  # Relative Humidity in %
    'NOx(GT)': np.random.uniform(10, 50, num_rows),
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to calculate AQI for each of the columns (simplified version)
def calculate_aqi(row):
    # Example simplified calculation for AQI from the provided features
    # Note: AQI formula is usually more complex and depends on various pollutants
    aqi_co = min(500, row['CO(GT)'] * 10)  # Adjust the calculation as needed
    aqi_c6h6 = min(500, row['C6H6(GT)'] * 20)
    aqi_nox = min(500, row['NOx(GT)'] * 5)
    aqi_temp = min(500, (row['T'] - 20) * 10)
    aqi_rh = min(500, (row['RH'] - 30) * 8)

    # Aggregate AQI (could be the max or some other calculation)
    return max(aqi_co, aqi_c6h6, aqi_nox, aqi_temp, aqi_rh)

# Apply AQI calculation to each row
df['AQI'] = df.apply(calculate_aqi, axis=1)

# Save the dataset to a CSV file
df.to_csv('air_quality_data.csv', index=False)

print("Dataset with AQI has been generated and saved to 'air_quality_data.csv'.")
