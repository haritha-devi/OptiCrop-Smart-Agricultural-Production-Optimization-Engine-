import pandas as pd

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

# Check for null values
print("Null Values in Each Column:\n")
print(df.isnull().sum())

# Check total null values
print("\nTotal Null Values:", df.isnull().sum().sum())

# Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates (if any)
df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)