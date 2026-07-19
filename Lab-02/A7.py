import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
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

df = df.drop(columns=["Record ID"])

data = df.iloc[:20]

n = len(data)

jc = np.zeros((n, n))
smc = np.zeros((n, n))
cos = np.zeros((n, n))

for i in range(n):
    for j in range(n):

        v1 = data.iloc[i]
        v2 = data.iloc[j]

        b1 = v1[binary_columns]
        b2 = v2[binary_columns]

        f11 = ((b1 == 1) & (b2 == 1)).sum()
        f10 = ((b1 == 1) & (b2 == 0)).sum()
        f01 = ((b1 == 0) & (b2 == 1)).sum()
        f00 = ((b1 == 0) & (b2 == 0)).sum()

        jc[i][j] = f11 / (f11 + f10 + f01)
        smc[i][j] = (f11 + f00) / (f11 + f10 + f01 + f00)

        cos[i][j] = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

plt.figure(figsize=(7, 5))
sns.heatmap(jc)
plt.title("Jaccard Coefficient")
plt.show()

plt.figure(figsize=(7, 5))
sns.heatmap(smc)
plt.title("Simple Matching Coefficient")
plt.show()

plt.figure(figsize=(7, 5))
sns.heatmap(cos)
plt.title("Cosine Similarity")
plt.show()