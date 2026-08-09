import pandas as pd

def label_encode(df, col):
    df = df.copy()
    df[col], _ = pd.factorize(df[col])
    return df


def one_hot_encode(df, col):
    df = df.copy()
    dummies = pd.get_dummies(df[col], prefix=col)
    df = df.drop(columns=[col]).join(dummies)
    return df


df = pd.read_excel("Lab-04/labdata.xlsx", sheet_name="marketing_campaign")

print("Original dataset shape:", df.shape)


label_df = label_encode(df, "Education")
label_df = label_encode(label_df, "Marital_Status")

print("\nAfter Label Encoding:")
print(label_df.head())
print("Shape:", label_df.shape)


onehot_df = one_hot_encode(df, "Education")
onehot_df = one_hot_encode(onehot_df, "Marital_Status")

print("\nAfter One-Hot Encoding:")
print(onehot_df.head())
print("Shape:", onehot_df.shape)