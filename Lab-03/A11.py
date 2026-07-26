import pandas as pd
import numpy as np

def euclidean_distance(point1, point2):
    distance = 0

    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2

    return distance ** 0.5


def kmeans(data, k):
    centroids = data[:k].copy()

    while True:
        clusters = [[] for i in range(k)]

        for point in data:
            distances = []

            for centroid in centroids:
                distances.append(euclidean_distance(point, centroid))

            index = distances.index(min(distances))
            clusters[index].append(point)

        new_centroids = []

        for cluster in clusters:
            new_centroids.append(np.mean(cluster, axis=0))

        new_centroids = np.array(new_centroids)

        if np.array_equal(centroids, new_centroids):
            break

        centroids = new_centroids

    return centroids, clusters


df = pd.read_excel(
    "Lab-03/labdata.xlsx",
    sheet_name="marketing_campaign"
)

features = ["Income", "Recency"]

df = df.dropna(subset=features)

data = df[features].values

centroids, clusters = kmeans(data, 3)

print("Final Centroids")
print(centroids)

for i in range(len(clusters)):
    print("Cluster", i + 1, ":", len(clusters[i]), "points")