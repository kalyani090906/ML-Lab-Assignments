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