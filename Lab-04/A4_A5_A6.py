import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import minkowski


def minkowski_dis(vec1, vec2, p):
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be of the same length")
    if p < 1:
        raise ValueError("p must be >= 1")

    total = sum(abs(a - b) ** p for a, b in zip(vec1, vec2))
    return total ** (1 / p)


df = pd.read_excel("Lab-04/labdata.xlsx", sheet_name="marketing_campaign")

data = df.select_dtypes(include="number").drop(columns=["ID"])

vec1 = data.iloc[0].tolist()
vec2 = data.iloc[1].tolist()

p_values = range(1, 11)
distances = []

print("A6: Comparing Own Function and Scipy Function")

for p in p_values:
    own = minkowski_dis(vec1, vec2, p)
    scipy = minkowski(vec1, vec2, p)

    distances.append(own)

    print("p =", p, "Own =", own, "Scipy =", scipy)

plt.plot(p_values, distances, marker="o")
plt.xlabel("p")
plt.ylabel("Minkowski Distance")
plt.title("Minkowski Distance for p = 1 to 10")
plt.grid()
plt.show()