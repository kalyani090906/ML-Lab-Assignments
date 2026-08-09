import pandas as pd
import math


def mean(values):
    values = list(values)
    total = 0
    for i in range(len(values)):
        total = total + values[i]
    return total / len(values)


def variance(values):
    values = list(values)
    avg = mean(values)
    var = 0
    for i in range(len(values)):
        var = var + ((values[i] - avg) ** 2)
    var = var / len(values)
    return var


def standard_deviation(values):
    return math.sqrt(variance(values))


def self_statistics(df):
    for col in df.columns:
        print(col, ":")
        print("Mean: ", mean(df[col]))
        var = variance(df[col])
        std = standard_deviation(df[col])
        print(f"Variance: {var:.3f}, S.D: {std:.3f}")
        print()


df = pd.read_excel("Lab Session Data.xlsx", sheet_name="marketing_campaign")
df = df.dropna()
df = df.drop(columns=['ID', 'Education', 'Marital_Status', 'Dt_Customer'])
self_statistics(df)