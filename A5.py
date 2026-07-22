import pandas as pd
import matplotlib.pyplot as plt


def minkowski_distance(v1, v2, p):
    distance = 0

    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i]) ** p

    distance = distance ** (1 / p)

    return distance




df = pd.read_excel("marketing_campaign.xlsx")
features = ["Income", "Recency"]

df = df.dropna(subset=features)


vector1 = df.loc[0, features].values
vector2 = df.loc[1, features].values

print("Vector 1:", vector1)
print("Vector 2:", vector2)

p_values = []
distances = []

# for p in range(1, 11):
#     distance = minkowski_distance(vector1, vector2, p)
#     p_values.append(p)
#     distances.append(distance)
#     print(f"p = {p}, Distance = {distance}")

# plt.plot(p_values, distances, marker='o')
# plt.title("Minkowski Distance vs Order (p)")
# plt.xlabel("Order (p)")
# plt.ylabel("Minkowski Distance")
# plt.grid(True)
# plt.show()