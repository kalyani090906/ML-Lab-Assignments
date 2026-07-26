import pandas as pd
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

    data = numeric_df[column].dropna().tolist()

    print("\nFeature:", column)
    print("Mean =", mean(data))
    print("Variance =", variance(data))
    print("Standard Deviation =", standard_deviation(data))