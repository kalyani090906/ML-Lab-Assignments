import random
from collections import Counter

def generate():
    nums = []
    for i in range(100):
        nums.append(random.randint(100,150))
    return nums

def find_mean(nums):
    return sum(nums) / len(nums)

def find_median(nums):
    nums.sort()
    n = len(nums)

    if n % 2 == 0:
        return (nums[n//2] + nums[n//2 - 1]) / 2
    else:
        return nums[n//2]

def find_mode(nums):
    data = Counter(nums)
    return data.most_common(1)[0][0]



nums = generate()
mean = find_mean(nums)
median = find_median(nums)
mode = find_mode(nums)

print(nums)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)