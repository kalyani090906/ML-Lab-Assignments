import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from A1_A2 import MyKNN as OwnKNN
from A1 import MyKNN as AIKNN, min_max_scale as ai_min_max_scale

# ---------------------------------------------------------
# Load and prepare data
# ---------------------------------------------------------
df = pd.read_csv("Lab-06/eeg_features.csv")
feature_cols = [c for c in df.columns if c not in ["subject", "label"]]

# Min-Max normalize (consistent across all 3 methods for fairness)
for col in feature_cols:
    col_min = df[col].min()
    col_max = df[col].max()
    df[col] = (df[col] - col_min) / (col_max - col_min) if col_max != col_min else 0.0

X = df[feature_cols].values.tolist()
y = df["label"].tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

N_RUNS = 10
K = 3

# ---------------------------------------------------------
# Helper: time + evaluate a model over N_RUNS
# ---------------------------------------------------------
def evaluate_model(name, fit_predict_fn):
    times = []
    preds = None
    for _ in range(N_RUNS):
        start = time.perf_counter()
        preds = fit_predict_fn()
        end = time.perf_counter()
        times.append(end - start)

    avg_time = sum(times) / len(times)
    acc = accuracy_score(y_test, preds)
    prec = precision_score(y_test, preds, zero_division=0)
    rec = recall_score(y_test, preds, zero_division=0)
    f1 = f1_score(y_test, preds, zero_division=0)

    return {
        "Model": name,
        "Accuracy": round(acc, 3),
        "Precision": round(prec, 3),
        "Recall": round(rec, 3),
        "F1-score": round(f1, 3),
        "Avg Time (s)": round(avg_time, 5),
    }


# ---------------------------------------------------------
# 1. Own hand-written kNN (Lab 5)
# ---------------------------------------------------------
def run_own():
    model = OwnKNN(k=K, p=2, sort_algorithm="merge")
    model.fit(X_train, y_train)
    return model.predict(X_test)


# ---------------------------------------------------------
# 2. sklearn kNN
# ---------------------------------------------------------
def run_sklearn():
    model = KNeighborsClassifier(n_neighbors=K)
    model.fit(X_train, y_train)
    return model.predict(X_test)


# ---------------------------------------------------------
# 3. AI-generated kNN (A1)
# ---------------------------------------------------------
def run_ai():
    model = AIKNN(k=K, p=2, algorithm="merge", weighted=False)
    model.fit(X_train, y_train)
    return model.predict(X_test)


# ---------------------------------------------------------
# Run all three and report
# ---------------------------------------------------------
results = [
    evaluate_model("Own kNN (Lab 5)", run_own),
    evaluate_model("sklearn kNN", run_sklearn),
    evaluate_model("AI-generated kNN (A1)", run_ai),
]

results_df = pd.DataFrame(results)
print("=" * 70)
print(f"A3: 3-WAY KNN PERFORMANCE COMPARISON (k={K}, averaged over {N_RUNS} runs)")
print("=" * 70)
print(results_df.to_string(index=False))

results_df.to_csv("A3_comparison_results.csv", index=False)
print("\nSaved to A3_comparison_results.csv")