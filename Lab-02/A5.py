import pandas as pd

df = pd.read_excel("lab2data.xlsx", sheet_name="thyroid0387_UCI")

binary_attributes = [
    "on thyroxine",
    "query on thyroxine",
    "on antithyroid medication",
    "sick",
    "pregnant",
    "thyroid surgery",
    "I131 treatment",
    "query hypothyroid",
    "query hyperthyroid",
    "lithium",
    "goitre",
    "tumor",
    "hypopituitary",
    "psych",
    "TSH measured",
    "T3 measured",
    "TT4 measured",
    "T4U measured",
    "FTI measured",
    "TBG measured"
]

binary_df = df[binary_attributes].replace({"t": 1, "f": 0})

vector1 = binary_df.iloc[0]
vector2 = binary_df.iloc[1]

f11 = ((vector1 == 1) & (vector2 == 1)).sum()
f10 = ((vector1 == 1) & (vector2 == 0)).sum()
f01 = ((vector1 == 0) & (vector2 == 1)).sum()
f00 = ((vector1 == 0) & (vector2 == 0)).sum()

jc = f11 / (f11 + f10 + f01)
smc = (f11 + f00) / (f11 + f10 + f01 + f00)

print("Jaccard Coefficient :", jc)
print("Simple Matching Coefficient :", smc)

# Observation:
# SMC is greater than or equal to JC because it considers both matching 1's and matching 0's.
# JC is more suitable for this dataset since the presence of a medical condition (1)
# is more informative than its absence (0).