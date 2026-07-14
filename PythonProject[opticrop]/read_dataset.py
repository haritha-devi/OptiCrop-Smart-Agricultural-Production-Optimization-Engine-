import pandas as pd

# Read the dataset
df = pd.read_csv("Crop_recommendation.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumns:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())