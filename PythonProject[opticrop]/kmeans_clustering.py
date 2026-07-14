import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Features
X = df[["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]]

# Train KMeans model
kmeans = KMeans(n_clusters=5, random_state=42)

df["Cluster"] = kmeans.fit_predict(X)

print(df[["label", "Cluster"]].head())

# Plot clusters
plt.figure(figsize=(8,6))

plt.scatter(
    df["temperature"],
    df["rainfall"],
    c=df["Cluster"],
    cmap="viridis"
)

plt.xlabel("Temperature")
plt.ylabel("Rainfall")
plt.title("K-Means Clustering")
plt.colorbar(label="Cluster")

plt.show()