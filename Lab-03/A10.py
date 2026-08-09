import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def mean(data):
    data = list(data)
    result = 0
    for i in range(len(data)):
        result = result + data[i]
    return result / len(data)


def variance(data):
    data = list(data)
    avg = mean(data)
    result = 0
    for i in range(len(data)):
        result = result + ((data[i] - avg) ** 2)
    result = result / len(data)
    return result


def histogram(dataset):
    col = "Income"
    values = dataset[col].dropna()
    freq, edges = np.histogram(values, bins=10)
    print("Histogram Counts: ", freq)
    print("Histogram Bins: ", edges)
    plt.hist(values, bins=10)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()


dataset = pd.read_excel("Lab Session Data.xlsx", sheet_name="marketing_campaign")
print("Feature = Income")
income = dataset['Income'].dropna()
print("Mean: ", mean(income))
print("Variance: ", variance(income))
histogram(dataset)