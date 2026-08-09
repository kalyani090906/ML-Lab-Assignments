import pandas as pd
import numpy as np


def mean(data):
    return sum(data) / len(data)


def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def std_dev(data):
    return variance(data) ** 0.5


def matrix_stats(data_2d):
    n_rows = len(data_2d)
    n_cols = len(data_2d[0])

    means = []
    variances = []
    std_devs = []

    for col in range(n_cols):
        column_values = [data_2d[row][col] for row in range(n_rows)]

        means.append(mean(column_values))
        variances.append(variance(column_values))
        std_devs.append(std_dev(column_values))

    return means, variances, std_devs


df = pd.read_excel("lab-04/labdata.xlsx", sheet_name="marketing_campaign")

data = df.select_dtypes(include="number").drop(columns=["ID"])

data_list = data.values.tolist()

means, variances, std_devs = matrix_stats(data_list)

print("Own Functions")
print("Mean:", means)
print("Variance:", variances)
print("Standard Deviation:", std_devs)

numpy_mean = data.mean(axis=0)
numpy_std = data.std(axis=0)

print("\nNumPy")
print("Mean:", numpy_mean.tolist())
print("Standard Deviation:", numpy_std.tolist())

print("\nComparison")
print("Mean same:", np.allclose(means, numpy_mean))
print("Standard Deviation same:", np.allclose(std_devs, numpy_std))