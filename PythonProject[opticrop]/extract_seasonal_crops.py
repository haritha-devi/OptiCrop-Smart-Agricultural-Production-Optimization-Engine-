import pandas as pd

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Assign seasons based on rainfall
def get_season(rainfall):
    if rainfall < 75:
        return "Summer"
    elif rainfall < 150:
        return "Winter"
    else:
        return "Monsoon"

# Create new Season column
df["Season"] = df["rainfall"].apply(get_season)

# Display first 10 rows
print(df[["label", "rainfall", "Season"]].head(10))

# Count crops by season
print("\nCrop Count by Season:")
print(df["Season"].value_counts())

# Save updated dataset
df.to_csv("Crop_recommendation_with_season.csv", index=False)

print("\nUpdated dataset saved as Crop_recommendation_with_season.csv")