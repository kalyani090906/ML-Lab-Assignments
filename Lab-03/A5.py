import pandas as pd
import matplotlib.pyplot as plt

def minkowski_distance(v1, v2, p):
    distance = 0
    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i]) ** p
    distance = distance ** (1 / p)
    return distance

df = pd.read_excel("Lab-03/labdata.xlsx", sheet_name="marketing_campaign")
df = df.dropna(subset=["Income", "Recency"])

vector1 = [df["Income"][0], df["Recency"][0]]
vector2 = [df["Income"][1], df["Recency"][1]]

print(vector1)
print(vector2)

p_values = []
distances = []

for p in range(1, 11):
    d = minkowski_distance(vector1, vector2, p)
    p_values.append(p)
    distances.append(d)
    print(p, d)

plt.plot(p_values, distances)
plt.xlabel("p")
plt.ylabel("Distance")
plt.show()