import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


def load_data(file_path):
    df = pd.read_excel(file_path, sheet_name="IRCTC Stock Price")
    return df


def numpy_statistics(price):
    return np.mean(price), np.var(price)


def custom_mean(price):
    total = 0

    for value in price:
        total += value

    return total / len(price)


def custom_variance(price):
    mean = custom_mean(price)
    variance = 0

    for value in price:
        variance += (value - mean) ** 2

    return variance / len(price)


def execution_time(func, values):
    total = 0

    for i in range(10):
        start = time.perf_counter()
        func(values)
        end = time.perf_counter()

        total += end - start

    return total / 10


def average_wednesday(df):
    wed = df[df["Day"] == "Wed"]
    return np.mean(wed["Price"])


def average_april(df):
    april = df[df["Month"] == "Apr"]
    return np.mean(april["Price"])


def loss_probability(df):
    loss_days = df[df["Chg%"] < 0]
    return len(loss_days) / len(df)


def profit_wednesday(df):
    wed = df[df["Day"] == "Wed"]
    profit = wed[wed["Chg%"] > 0]

    return len(profit) / len(df)

def conditional_profit(df):
    wed = df[df["Day"] == "Wed"]
    profit = wed[wed["Chg%"] > 0]

    return len(profit) / len(wed)


def plot_scatter(df):
    plt.scatter(df["Day"], df["Chg%"])
    plt.title("Day vs Change Percentage")
    plt.xlabel("Day")
    plt.ylabel("Chg%")
    plt.show()


file_path = "lab2data.xlsx"

df = load_data(file_path)

price = df["Price"]

mean_np, var_np = numpy_statistics(price)

print("Mean (NumPy):", mean_np)
print("Mean (Custom):", custom_mean(price))

print("Variance (NumPy):", var_np)
print("Variance (Custom):", custom_variance(price))

print("\nAverage Execution Time")

print("NumPy Mean:", execution_time(np.mean, price))
print("Custom Mean:", execution_time(custom_mean, price))

print("NumPy Variance:", execution_time(np.var, price))
print("Custom Variance:", execution_time(custom_variance, price))

wed_mean = average_wednesday(df)
apr_mean = average_april(df)

print("Overall Mean:", mean_np)
print("Wednesday Mean:", wed_mean)
print("April Mean:", apr_mean)

print("Probability of Loss:", loss_probability(df))
print("Probability of Profit on Wednesday:", profit_wednesday(df))
print("Conditional Probability of Profit given Wednesday:", conditional_profit(df))

plot_scatter(df)