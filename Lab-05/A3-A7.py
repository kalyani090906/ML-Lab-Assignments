import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


from A1_A2 import MyKNN
df = pd.read_csv("Lab-05/eeg_features.csv")

feature_cols = [c for c in df.columns if c not in ["subject", "label"]]

X = df[feature_cols].values.tolist()
y = df["label"].tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
print(f"Train size: {len(X_train)}, Test size: {len(X_test)}")

sklearn_knn = KNeighborsClassifier(n_neighbors=3)
sklearn_knn.fit(X_train, y_train)
sklearn_accuracy = sklearn_knn.score(X_test, y_test)
print(f"\nsklearn kNN (k=3) accuracy: {sklearn_accuracy:.3f}")
print("sklearn predictions:", sklearn_knn.predict(X_test))


my_knn = MyKNN(k=3, p=2, sort_algorithm="merge")
my_knn.fit(X_train, y_train)
my_accuracy = my_knn.score(X_test, y_test)
print(f"\nOwn kNN (k=3) accuracy: {my_accuracy:.3f}")
print("Own predictions:", my_knn.predict(X_test))

print(f"\nActual test labels:      {y_test}")