import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Features
X = df.drop("label", axis=1)

# Target
y = df["label"]

# Split dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Features:", X_train.shape)
print("Testing Features :", X_test.shape)
print("Training Labels  :", y_train.shape)
print("Testing Labels   :", y_test.shape)