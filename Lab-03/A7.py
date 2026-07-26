import pandas as pd
import numpy as np
import math


def dot_product(A, B):
    result = 0

    for i in range(len(A)):
        result += A[i] * B[i]

    return result


def euclidean_norm(A):
    result = 0

    for i in range(len(A)):
        result += A[i] ** 2

    return math.sqrt(result)


df = pd.read_excel(
    "Lab-03/labdata.xlsx",
    sheet_name="marketing_campaign"
)


features = ["Income", "Recency"]


df = df.dropna(subset=features)


A = df.iloc[0][features].values
B = df.iloc[1][features].values


my_dot = dot_product(A, B)
my_norm_A = euclidean_norm(A)
my_norm_B = euclidean_norm(B)


numpy_dot = np.dot(A, B)
numpy_norm_A = np.linalg.norm(A)
numpy_norm_B = np.linalg.norm(B)

print("Vector A:", A)
print("Vector B:", B)

print("\nDot Product")
print("Own Function :", my_dot)
print("NumPy        :", numpy_dot)

print("\nEuclidean Norm of Vector A")
print("Own Function :", my_norm_A)
print("NumPy        :", numpy_norm_A)

print("\nEuclidean Norm of Vector B")
print("Own Function :", my_norm_B)
print("NumPy        :", numpy_norm_B)