
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


























def label_encode_column(df_in, column_name):
    """Label-encodes a single column and returns a new dataframe (no mutation)."""
    df_out = df_in.copy()
    df_out = df_out.replace('?', np.nan)
 
    unique_values = df_out[column_name].unique()
    mapping = {value: i for i, value in enumerate(unique_values)}
 
    df_out[column_name] = df_out[column_name].map(mapping)
    return df_out
 
 
def one_hot_encode_columns(df_in, nominal_columns):
    """
    One-hot encodes multiple columns at once using pd.get_dummies(),
    then drops the original columns and joins the encoded ones back in.
    """
    df_out = df_in.copy()
    df_out = df_out.replace('?', np.nan)
 
    for column_name in nominal_columns:
        dummies = pd.get_dummies(df_out[column_name], dtype=int)
        df_out = pd.concat([df_out, dummies], axis=1)
        df_out = df_out.drop(column_name, axis=1)
 
    return df_out
 
 
# Example usage, mirroring Code 2's original workflow:
 
nominal = [
    'Marital_Status', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5',
    'AcceptedCmp1', 'AcceptedCmp2', 'Complain', 'Response'
]
 
df_label_encoded = label_encode_column(df, "Education")
print("\nAfter Label Encoding (Code 2 style)")
print(df_label_encoded["Education"].head())
 
df_one_hot_encoded = one_hot_encode_columns(df_label_encoded, nominal)
print("\nAfter One-Hot Encoding (Code 2 style, multiple columns at once)")
print(df_one_hot_encoded.head())