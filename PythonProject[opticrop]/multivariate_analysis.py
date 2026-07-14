import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Use FiveThirtyEight style
plt.style.use("fivethirtyeight")

# Correlation matrix
correlation = df.drop("label", axis=1).corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation,
            annot=True,
            cmap="coolwarm",
            linewidths=0.5)

plt.title("Correlation Heatmap of Agricultural Features")
plt.show()