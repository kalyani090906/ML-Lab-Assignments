def minkowski_distance(v1, v2, p):
    distance = 0

    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i]) ** p

    distance = distance ** (1 / p)

    if p == 1:
        dis_type = "Manhattan"
    elif p == 2:
        dis_type = "Euclidean"
    else:
        dis_type = "Minkowski"

    return distance, dis_type

A = [3,4,5]
B = [9,8,7]

print(minkowski_distance(A,B,1))
print(minkowski_distance(A,B,2))
print(minkowski_distance(A,B,3))