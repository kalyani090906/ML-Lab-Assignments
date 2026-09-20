import pandas as pd
import numpy as np


df = pd.read_csv("eeg_features.csv")
print(df['label'].value_counts())

def calculate_entropy(labels):
    counts = pd.Series(labels).value_counts()
    probabilities = counts / len(labels)
    
    entropy = 0
    for p in probabilities:
        entropy += -p * np.log2(p)
    
    return entropy

def calculate_gini(labels):
    counts = pd.Series(labels).value_counts()
    probabilities = counts / len(labels)
    
    gini = 1
    for p in probabilities:
        gini -= p ** 2
    
    return gini

def bin_feature(values, bin_type="equal_width", n_bins=4):
    if bin_type == "equal_width":
        min_val = min(values)
        max_val = max(values)
        data_range = max_val - min_val

        
        width = data_range / n_bins
        bin_assignments = []

        for x in values:
            shifted_value = x - min_val
            bin_idx = int(shifted_value / width)
            if bin_idx >= n_bins:
                bin_idx = n_bins - 1
            bin_assignments.append(bin_idx)

        return bin_assignments

    elif bin_type == "equal_frequency":
        bin_assignments = pd.qcut(values, q=n_bins, labels=False, duplicates="drop")
        return list(bin_assignments)

    



print(df['label'].value_counts())
print("Entropy:", calculate_entropy(df['label'].tolist()))
print("Gini:", calculate_gini(df['label'].tolist()))
print(bin_feature(df["state0_duration"].tolist(), bin_type="equal_width", n_bins=4))