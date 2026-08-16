import math
import pandas as pd
import numpy as np

# a. Encoding

def encode_if_categorical(df, column):
    if df[column].dtype == object:
        unique_values = df[column].unique()
        mapping = {value: i for i, value in enumerate(unique_values)}
        return df[column].map(mapping)
    return df[column]

# b. Data Imputation

def impute_column(column, method="mean"):
    filled = column.copy()
    if method == "mean":
        fill_value = column.mean()
    elif method == "median":
        fill_value = column.median()
    elif method == "mode":
        fill_value = column.mode()[0]
    else:
        raise ValueError("method must be 'mean', 'median', or 'mode'")
    return filled.fillna(fill_value)


# c. Distance Calculation

def minkowski_distance(v1, v2, p):
    distance = 0
    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i]) ** p
    return distance ** (1 / p)

# d. Sorting Algorithms(bubble,merge,quick)

def bubble_sort(items):
    items = items.copy()
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][0] > items[j + 1][0]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(items):
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    left = [x for x in items if x[0] < pivot[0]]
    middle = [x for x in items if x[0] == pivot[0]]
    right = [x for x in items if x[0] > pivot[0]]
    return quick_sort(left) + middle + quick_sort(right)


SORT_FUNCTIONS = {
    "bubble": bubble_sort,
    "merge": merge_sort,
    "quick": quick_sort,
}


def sort_by_distance(distance_label_pairs, algorithm="merge"):
    if algorithm not in SORT_FUNCTIONS:
        raise ValueError(f"algorithm must be one of {list(SORT_FUNCTIONS.keys())}")
    return SORT_FUNCTIONS[algorithm](distance_label_pairs)

# e. Identify k Nearest Neighbors 
def get_k_neighbors(sorted_distance_label_pairs, k):
    return sorted_distance_label_pairs[:k]

# f. Class Evaluation and Assignment

def majority_vote(k_neighbors):
    votes = {}
    for distance, label in k_neighbors:
        votes[label] = votes.get(label, 0) + 1

    max_votes = max(votes.values())
    tied_classes = [label for label, count in votes.items() if count == max_votes]

    if len(tied_classes) == 1:
        return tied_classes[0]

    for distance, label in k_neighbors:
        if label in tied_classes:
            return label


#KNN

class MyKNN:
    def __init__(self, k=3, p=2, sort_algorithm="merge"):
        self.k = k
        self.p = p
        self.sort_algorithm = sort_algorithm
        self.X_train = None
        self.y_train = None

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def _predict_one(self, x):
        distance_label_pairs = []
        for i in range(len(self.X_train)):
            dist = minkowski_distance(x, self.X_train[i], self.p)
            distance_label_pairs.append((dist, self.y_train[i]))

        sorted_pairs = sort_by_distance(distance_label_pairs, self.sort_algorithm)
        neighbors = get_k_neighbors(sorted_pairs, self.k)
        return majority_vote(neighbors)

    def predict(self, X_test):
        return [self._predict_one(x) for x in X_test]

    def score(self, X_test, y_test):
        predictions = self.predict(X_test)
        correct = sum(1 for pred, true in zip(predictions, y_test) if pred == true)
        return correct / len(y_test)


#Weighted KNN

def weighted_vote(k_neighbors):
    weighted_votes = {}
    for distance, label in k_neighbors:
        weight = 1 / (distance + 1e-6)
        weighted_votes[label] = weighted_votes.get(label, 0) + weight

    max_weight = max(weighted_votes.values())
    tied_classes = [label for label, w in weighted_votes.items() if w == max_weight]

    if len(tied_classes) == 1:
        return tied_classes[0]

    for distance, label in k_neighbors:
        if label in tied_classes:
            return label


class MyWeightedKNN(MyKNN):
    def _predict_one(self, x):
        distance_label_pairs = []
        for i in range(len(self.X_train)):
            dist = minkowski_distance(x, self.X_train[i], self.p)
            distance_label_pairs.append((dist, self.y_train[i]))

        sorted_pairs = sort_by_distance(distance_label_pairs, self.sort_algorithm)
        neighbors = get_k_neighbors(sorted_pairs, self.k)
        return weighted_vote(neighbors)    




df = pd.read_csv("Lab-05/eeg_features.csv")
feature_cols = [
    col
    for col in df.columns
    if col not in ["subject", "label"]
]

for col in feature_cols:

    df[col] = encode_if_categorical(df, col)

    df[col] = impute_column(
        df[col],
        method="mean"
    )


X = df[feature_cols].values.tolist()

y = df["label"].tolist()

print("Number of samples:", len(X))
print("Number of features:", len(feature_cols))
print("Classes:", sorted(set(y)))