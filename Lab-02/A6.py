import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_excel("lab2data.xlsx", sheet_name="thyroid0387_UCI")

df = df.replace("?", pd.NA)

binary_columns = [
    "on thyroxine", "query on thyroxine", "on antithyroid medication",
    "sick", "pregnant", "thyroid surgery", "I131 treatment",
    "query hypothyroid", "query hyperthyroid", "lithium",
    "goitre", "tumor", "hypopituitary", "psych",
    "TSH measured", "T3 measured", "TT4 measured",
    "T4U measured", "FTI measured", "TBG measured"
]

df[binary_columns] = df[binary_columns].replace({"t": 1, "f": 0})


numeric_columns = ["age", "TSH", "T3", "TT4", "T4U", "FTI", "TBG"]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())


encoder = LabelEncoder()

for col in ["sex", "referral source", "Condition"]:
    df[col] = encoder.fit_transform(df[col])

vector1 = df.iloc[0]
vector2 = df.iloc[1]

dot_product = np.dot(vector1, vector2)
magnitude1 = np.linalg.norm(vector1)
magnitude2 = np.linalg.norm(vector2)

cosine_similarity = dot_product / (magnitude1 * magnitude2)

print("Cosine Similarity :", cosine_similarity)