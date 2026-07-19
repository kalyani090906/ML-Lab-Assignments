import pandas as pd

df = pd.read_excel("lab2data.xlsx", sheet_name="thyroid0387_UCI")

df = df.replace("?", pd.NA)


numeric_columns = ["age", "TSH", "T3", "TT4", "T4U", "FTI", "TBG"]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

categorical_columns = ["sex", "referral source", "Condition"]

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print(df.isnull().sum())