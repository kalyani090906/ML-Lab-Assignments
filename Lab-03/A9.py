import pandas as pd
import numpy as np


def numpy_statistics(df):
    print("Numpy Mean: ")
    print(np.mean(df, axis=0))
    print("Numpy Standard Deviation: ")
    print(np.std(df, axis=0))


df = pd.read_excel("Lab Session Data.xlsx", sheet_name="marketing_campaign")
df = df.dropna()
df = df.drop(columns=['ID', 'Education', 'Marital_Status', 'Dt_Customer'])

print("Compare with inbuilt Numpy functions")
numpy_statistics(df)