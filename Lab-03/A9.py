import pandas as pd
import numpy as np
import math


def mean(data):
    total = 0
    for value in data:
        total += value
    return total / len(data)


def variance(data):
    avg = mean(data)
    total = 0
    for value in data:
        total += (value - avg) ** 2
    return total / len(data)


def standard_deviation(data):
    return math.sqrt(variance(data))

df = pd.read_excel(
    "Lab-03/labdata.xlsx",
    sheet_name="marketing_campaign"
)

numeric_df = df.select_dtypes(include="number")

for column in numeric_df.columns:

    data = numeric_df[column].dropna().values

    my_mean = mean(data)
    my_std = standard_deviation(data)

 
    numpy_mean = np.mean(data)
    numpy_std = np.std(data)

    print("\nFeature:", column)

    print("Mean")
    print("Own Function :", my_mean)
    print("NumPy        :", numpy_mean)

    print("Standard Deviation")
    print("Own Function :", my_std)
    print("NumPy        :", numpy_std)