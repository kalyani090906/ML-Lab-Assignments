import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_excel("lab2data.xlsx", sheet_name="thyroid0387_UCI")

df = df.replace("?", pd.NA)

numeric_columns = ["age", "TSH", "T3", "TT4", "T4U", "FTI", "TBG"]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

scaler = MinMaxScaler()

df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

print(df[numeric_columns].head())