import pandas as pd
import numpy as np

def load_purchase_data(file_path):
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

def main():
    file_path = "Lab Session Data _lab2.xlsx"
   
    df = load_purchase_data(file_path)

    X, y = create_matrices(df)
    print(X)
    print(y)

    rank = calc_rank(X)
    print("Rank of X:", rank)

    costs = calc_product_costs(X, y)

    print("Product Costs:")
    print("Candy:", costs[0])
    print("Mango per Kg:", costs[1])
    print("Milk Packet:", costs[2])