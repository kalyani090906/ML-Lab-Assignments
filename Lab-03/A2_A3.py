
import pandas as pd
import numpy as np
def load_data():
    df = pd.read_excel(
        "Lab-03/labdata.xlsx",
        sheet_name="marketing_campaign"
    )
    return df
df = load_data()

def label_encode(column):
    unique_values = column.unique()

    mapping = {}

    for i, value in enumerate(unique_values):
        mapping[value] = i

    return column.map(mapping)

def one_hot_encode(column):
    unique_values = column.unique()

    encoded_df = pd.DataFrame()

    for value in unique_values:
        encoded_df[value] = (column == value).astype(int)

    return encoded_df

print("Before Label Encoding")
print(df["Education"].head())

encoded_education = label_encode(df["Education"])

print("After Label Encoding")
print(encoded_education.head())

print("Before One-Hot Encoding")
print(df["Marital_Status"].head())

encoded_marital = one_hot_encode(df["Marital_Status"])

print("After One-Hot Encoding")
print(encoded_marital.head())