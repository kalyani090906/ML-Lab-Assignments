import pandas as pd
from scipy.spatial.distance import minkowski

def minkowski_distance(vector1, vector2, p):
    distance = 0

    for i in range(len(vector1)):
        distance += abs(vector1[i] - vector2[i]) ** p

    distance = distance ** (1 / p)

    return distance


df = pd.read_excel("Lab-03/labdata.xlsx",
        sheet_name="marketing_campaign"
    )

features = ["Income", "Recency"]

df = df.dropna(subset=features)

vector1 = df.loc[0, features].values
vector2 = df.loc[1, features].values

print("p")
print("Own Function")
print("SciPy Function")

for p in range(1, 11):
    own_distance = minkowski_distance(vector1, vector2, p)
    scipy_distance = minkowski(vector1, vector2, p)

    print(f"{p}")
    print(f"{own_distance:.4f}")
    print(f"{scipy_distance:.4f}")