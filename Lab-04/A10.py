import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def mean(data):
    total = 0

    for value in data:
        total += value

    return total / len(data)


def variance(data):
    avg = mean(data)
    total = 0

    for value in data:
        total += (value - avg) ** 2

    return total / len(data)


def histogram(data, bins):
    counts, bin_edges = np.histogram(data, bins=bins)

    plt.hist(data, bins=bin_edges, edgecolor='black')
    plt.xlabel("Income")
    plt.ylabel("Frequency")
    plt.title("Histogram of Income")
    plt.show()

    return bin_edges, counts



df = pd.read_excel("labdata(1).xlsx", sheet_name="marketing_campaign")


data = df["Income"].dropna().tolist()


bin_edges, counts = histogram(data, 10)


avg = mean(data)
var = variance(data)

print("Bin Edges:", bin_edges)
print("Frequency:", counts)
print("Mean:", avg)
print("Variance:", var)