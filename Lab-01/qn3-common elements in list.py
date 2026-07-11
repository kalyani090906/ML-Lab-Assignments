def common_elements(l1, l2):
    count = 0

    for item in l1:
        if item in l2:
            count += 1
    return count


list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

count = common_elements(list1, list2)

print("Number of common elements =", count)