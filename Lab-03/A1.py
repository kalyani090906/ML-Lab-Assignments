import pandas as pd
import numpy as np

def load_data():
    df = pd.read_excel(
        "Lab-03/labdata.xlsx",
        sheet_name="marketing_campaign"
    )
    return df


def categorical_columns(df):
    return df.select_dtypes(include=["object"]).columns


def numerical_columns(df):
    return df.select_dtypes(include=np.number).columns


df = load_data()

print("Column Names:")
print(df.columns)

print("Categorical Columns:")
print(categorical_columns(df))

print("Numerical Columns:")
print(numerical_columns(df))



"""
Classification:

Nominal:
ID, Marital_Status, AcceptedCmp1-5,Complain, Response

Ordinal:
Education

Interval:
Year_Birth, Dt_Customer

Ratio:
Income, Kidhome, Teenhome, Recency....
"""