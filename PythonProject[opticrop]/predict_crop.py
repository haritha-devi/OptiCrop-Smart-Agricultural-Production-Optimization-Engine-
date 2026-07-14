import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Sample input
sample = pd.DataFrame({
    "N": [90],
    "P": [42],
    "K": [43],
    "temperature": [20.879744],
    "humidity": [82.002744],
    "ph": [6.502985],
    "rainfall": [202.935536]
})

prediction = model.predict(sample)

print("Recommended Crop:", prediction[0])