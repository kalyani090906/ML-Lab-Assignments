import pandas as pd
import numpy as np

def data(file_path):
    df = pd.read_excel(file_path, sheet_name="Purchase data")
    return df

def create_matrices(df):
    X = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]].to_numpy()
    y = df["Payment (Rs)"].to_numpy()
    return X, y


def calc_rank(X):
    return np.linalg.matrix_rank(X)


def calc_product_costs(X, y):
    X_pinv = np.linalg.pinv(X)
    cost = X_pinv @ y
    return cost


file_path = "lab2data.xlsx"
   
df = data(file_path)

X, y = create_matrices(df)
print(X)
print(y)

rank = calc_rank(X)
print("Rank of X:", rank)

costs = calc_product_costs(X, y)

    
print("Candy","Mango per Kg", "Milk Packet")
print(costs)
   