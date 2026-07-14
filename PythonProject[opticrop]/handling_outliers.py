import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Use FiveThirtyEight style
plt.style.use("fivethirtyeight")

# Numerical columns
columns = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

# Create box plots
plt.figure(figsize=(14, 8))
df.boxplot(column=columns)

plt.title("Box Plot for Detecting Outliers")
plt.xticks(rotation=45)
plt.grid(True)

plt.show()