import numpy as np


def dot_prod(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must be of the same length")

    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total


def vec_norm(a):
    total = 0
    for i in range(len(a)):
        total += a[i] ** 2
    return total ** 0.5


A = [1, 2, 3]
B = [4, 5, 6]

print("Dot Product:")
print("Own function:", dot_prod(A, B))
print("NumPy:", np.dot(A, B))

print("\nEuclidean Norm:")
print("Own function A:", vec_norm(A))
print("NumPy A:", np.linalg.norm(A))

print("Own function B:", vec_norm(B))
print("NumPy B:", np.linalg.norm(B))