import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(
    "Lab-03/labdata.xlsx",
    sheet_name="marketing_campaign"
)

data = df["Income"].dropna()

mean = np.mean(data)
variance = np.var(data)

hist, bins = np.histogram(data, bins=10)

print("Histogram Counts:", hist)
print("Bin Edges:", bins)

print("Mean:", mean)
print("Variance:", variance)

plt.hist(data, bins=10)
plt.title("Histogram of Income")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()