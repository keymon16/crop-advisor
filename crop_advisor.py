import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings("ignore")

# Step 1: Load the dataset
data = pd.read_csv("Crop_recommendation.csv")

# Step 2: Split data into input (X) and output (y)
X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = data['label']

# Step 3: Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 4: Take user input
print("Enter the following values to get crop recommendation:")
N = float(input("Nitrogen (N): "))
P = float(input("Phosphorous (P): "))
K = float(input("Potassium (K): "))
temperature = float(input("Temperature (°C): "))
humidity = float(input("Humidity (%): "))
ph = float(input("Soil pH: "))
rainfall = float(input("Rainfall (mm): "))

# Step 5: Predict the crop
input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
prediction = model.predict(input_data)
print("\n🌾 Recommended Crop to Grow:", prediction[0])
