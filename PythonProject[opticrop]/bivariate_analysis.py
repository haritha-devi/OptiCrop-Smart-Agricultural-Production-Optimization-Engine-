import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Use FiveThirtyEight style
plt.style.use("fivethirtyeight")

# Scatter plot
plt.figure(figsize=(10, 6))

for crop in df["label"].unique():
    crop_data = df[df["label"] == crop]
    plt.scatter(
        crop_data["humidity"],
        crop_data["temperature"],
        label=crop,
        s=20
    )

plt.xlabel("Humidity")
plt.ylabel("Temperature")
plt.title("Humidity vs Temperature by Crop")

# Show legend outside graph
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=7)

plt.tight_layout()
plt.show()