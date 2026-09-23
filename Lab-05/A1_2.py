import numpy as np
import pandas as pd
import math


def data_split(X, Y, test_size=0.2, seed=42):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(X))
    n_test = int(len(X) * test_size)
    test_idx = idx[:n_test]
    train_idx = idx[n_test:]
    X_train = X.iloc[train_idx].reset_index(drop=True)
    X_test = X.iloc[test_idx].reset_index(drop=True)
    y_train = Y.iloc[train_idx].reset_index(drop=True)
    y_test = Y.iloc[test_idx].reset_index(drop=True)
    return X_train, X_test, y_train, y_test


def missing_values(X_train, X_test, numerical, categorical):
    X_train = X_train.replace("?", np.nan)
    X_test = X_test.replace("?", np.nan)
    for col in numerical:
        X_train[col] = pd.to_numeric(X_train[col], errors="coerce")
        X_test[col] = pd.to_numeric(X_test[col], errors="coerce")
        mean1 = X_train[col].mean()
        X_train[col] = X_train[col].fillna(mean1)
        X_test[col] = X_test[col].fillna(mean1)
    for col in categorical:
        mode1 = X_train[col].mode()[0]
        X_train[col] = X_train[col].fillna(mode1)
        X_test[col] = X_test[col].fillna(mode1)
    return X_train, X_test


def label_encoding(X_train, X_test, categorical):
    for col in categorical:
        mapping = {}
        for value in X_train[col]:
            if value not in mapping:
                mapping[value] = len(mapping)
        X_train[col] = X_train[col].map(mapping)
        X_test[col] = X_test[col].map(mapping).fillna(-1)
    return X_train, X_test


def distance(train_data, point):
    a = list(train_data)
    total = 0
    for i in range(len(a)):
        total = total + ((a[i] - point[i]) ** 2)
    return math.sqrt(total)


def distance_train(train_data, point):
    dist = []
    for i in range(len(train_data)):
        temp = distance(train_data[i], point)
        dist.append((temp, i))
    return dist


def heap_sort(arr):
    a = arr.copy()

    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and a[l] > a[largest]:
            largest = l
        if r < n and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(n, largest)

    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(i, 0)
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    a = arr.copy()

    def partition(low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    stack = [(0, len(a) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))
    return a


def choose_sorting():
    print("\nChoose sorting algorithm: \n1. Quick Sort \n2. Merge Sort \n3. Heap Sort \n")
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            return quick_sort
        case 2:
            return merge_sort
        case 3:
            return heap_sort
        case _:
            print("Invalid")
            return None


def k_neighbour(sorted_dist, k):
    return sorted_dist[:k]


def k_classes(neighbours, y_train):
    class_type = []
    for dist, index in neighbours:
        class_type.append(y_train.iloc[index])
    return class_type


def winning_class(class_type):
    votes = {}
    for c in class_type:
        votes[c] = votes.get(c, 0) + 1
    max_votes = max(votes.values())
    tied = [c for c in votes if votes[c] == max_votes]
    if len(tied) == 1:
        return tied[0]
    for c in class_type:
        if c in tied:
            return c


p = pd.read_csv("Lab-05/eeg_features.csv")
X = p.drop(columns=["subject", "label"], errors="ignore")
Y = p["label"]

numerical = []
categorical = []
for col in X.columns:
    converted = pd.to_numeric(X[col].replace("?", np.nan), errors="coerce")
    if converted.notna().sum() == X[col].replace("?", np.nan).notna().sum():
        numerical.append(col)
    else:
        categorical.append(col)

X_train, X_test, y_train, y_test = data_split(X, Y)
X_train, X_test = missing_values(X_train, X_test, numerical, categorical)
X_train, X_test = label_encoding(X_train, X_test, categorical)

features = X_train.columns
train_data = X_train[features].astype(float).values.tolist()
test_data = X_test[features].astype(float).values.tolist()


def main():
    print("Train samples:", len(train_data), "| Test samples:", len(test_data))
    print("Features:", len(features), "| Classes:", sorted(set(Y)))

    sorting_function = choose_sorting()
    if sorting_function is None:
        return
    k = int(input("\nEnter the value of k: "))

    predict_all = []
    for data in test_data:
        dist = distance_train(train_data, data)
        sorted_dist = sorting_function(dist)
        neighbours = k_neighbour(sorted_dist, k)
        class_type = k_classes(neighbours, y_train)
        prediction = winning_class(class_type)
        predict_all.append(prediction)

    print("\nPredicted count per class:")
    for c in sorted(set(y_train)):
        print(c, ": ", predict_all.count(c))

    correct = sum(1 for pred, true in zip(predict_all, y_test) if pred == true)
    print("\nAccuracy:", round(correct / len(y_test) * 100, 2), "%")


if __name__ == "__main__":
    main()