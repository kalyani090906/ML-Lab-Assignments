import math
import pandas as pd
import numpy as np


def dot_product(vec1, vec2, length):
    vec1 = list(vec1)
    vec2 = list(vec2)
    total = 0
    for i in range(length):
        total += vec1[i] * vec2[i]
    return total


def euclidean_norm(vec, length):
    vec = list(vec)
    total = 0
    for i in range(length):
        total += vec[i] * vec[i]
    total = math.sqrt(total)
    return total


A = [3, 7, 2, 9, 5]
B = [8, 1, 6, 4, 3]
n = len(A)

dot = dot_product(A, B, n)
euclidean_A = euclidean_norm(A, n)

print("Self Dot product: ", dot)
print("Numpy Dot Product: ", np.dot(A, B))
print("Self Euclidean Norm A: ", euclidean_A)
print("Numpy Euclidean Norm A: ", np.linalg.norm(A))