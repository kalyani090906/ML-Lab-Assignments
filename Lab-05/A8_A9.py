import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from A1_A2 import MyKNN, MyWeightedKNN

df = pd.read_csv("Lab-05/eeg_features.csv")

feature_cols = [c for c in df.columns if c not in ["subject", "label"]]

for col in feature_cols:
    col_min = df[col].min()
    col_max = df[col].max()
    df[col] = (df[col] - col_min) / (col_max - col_min) if col_max != col_min else 0

X = df[feature_cols].values.tolist()

y = df["label"].tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

k_values = range(1, 11)

sklearn_acc = []
own_acc = []
weighted_acc = []


for k in k_values:

    
    sk = KNeighborsClassifier(n_neighbors=k)
    sk.fit(X_train, y_train)
    sklearn_acc.append(sk.score(X_test, y_test))

    mk = MyKNN(k=k, p=2, sort_algorithm="merge")
    mk.fit(X_train, y_train)
    own_acc.append(mk.score(X_test, y_test))

    wk = MyWeightedKNN(k=k, p=2, sort_algorithm="merge")
    wk.fit(X_train, y_train)
    weighted_acc.append(wk.score(X_test, y_test))

print("\nk   sklearn   My kNN   Weighted kNN")

for i, k in enumerate(k_values):
    print(
        k,
        f"{sklearn_acc[i]:.3f}",
        f"{own_acc[i]:.3f}",
        f"{weighted_acc[i]:.3f}"
    )

plt.plot(k_values, sklearn_acc, marker="o", label="sklearn kNN")
plt.plot(k_values, own_acc, marker="s", label="My kNN")
plt.plot(k_values, weighted_acc, marker="^", label="Weighted kNN")

plt.xlabel("k")
plt.ylabel("Accuracy")

plt.legend()
plt.show()