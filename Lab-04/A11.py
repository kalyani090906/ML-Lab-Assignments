import random


def initialize_centroids(data, k, seed=None):
    if seed is not None:
        random.seed(seed)

    centroids = random.sample(data, k)

    return [list(c) for c in centroids]


def euclidean_distance(a, b):
    total = 0

    for i in range(len(a)):
        total += (a[i] - b[i]) ** 2

    return total ** 0.5


def assign_clusters(data, centroids):
    labels = []

    for point in data:
        distances = []

        for centroid in centroids:
            distances.append(euclidean_distance(point, centroid))

        nearest = distances.index(min(distances))
        labels.append(nearest)

    return labels


def update_centroids(data, labels, k):
    n_features = len(data[0])

    sums = [[0] * n_features for _ in range(k)]
    counts = [0] * k

    for point, label in zip(data, labels):
        counts[label] += 1

        for j in range(n_features):
            sums[label][j] += point[j]

    new_centroids = []

    for i in range(k):
        if counts[i] == 0:
            new_centroids.append(None)
        else:
            centroid = []

            for j in range(n_features):
                centroid.append(sums[i][j] / counts[i])

            new_centroids.append(centroid)

    return new_centroids


def kmeans(data, k, max_iters=100, tol=0.0001, seed=None):

    centroids = initialize_centroids(data, k, seed)

    for iteration in range(max_iters):

        # Assign every point to nearest centroid
        labels = assign_clusters(data, centroids)

        # Calculate new centroids
        new_centroids = update_centroids(data, labels, k)

        # If a cluster is empty, keep its old centroid
        for i in range(k):
            if new_centroids[i] is None:
                new_centroids[i] = centroids[i]

        # Check how much centroids changed
        shift = 0

        for i in range(k):
            shift += euclidean_distance(centroids[i], new_centroids[i])

        centroids = new_centroids

        # Stop if centroids have stopped changing
        if shift < tol:
            break

    return centroids, labels


# Example
data = [
    [1, 2],
    [2, 1],
    [3, 2],
    [8, 9],
    [9, 8],
    [10, 9]
]

centroids, labels = kmeans(data, 2, seed=42)

print("Final Centroids:")
print(centroids)

print("Cluster Labels:")
print(labels)