import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("lab2data.xlsx", sheet_name="thyroid0387_UCI")



# Q1. Identify the datatype of each attribute

print("Dataset Information")
print(df.info())

# Observation:
# Numerical attributes are stored as int64 or float64.
# Categorical attributes are stored as object datatype.
#
# Attribute Type and Encoding:
# age, TSH, T3, TT4, T4U, FTI, TBG -> Ratio (No Encoding)
# sex -> Nominal -> One-Hot Encoding
# referral source -> Nominal -> One-Hot Encoding
# Binary attributes (on thyroxine, sick, pregnant, tumor, etc.) -> Nominal (Binary) -> Label Encoding
# Condition/Class -> Nominal -> Label Encoding
# No ordinal attributes are present in this dataset.



# Q2. Study the data range
print("\nData Range")
print(df.describe())

# Observation:
# The maximum age is unusually high, indicating the presence of outliers.
# Some numerical attributes such as TSH, T3, TT4, T4U, FTI and TBG are stored as object datatype because they contain '?' values.



# Q3. Identify missing values


print("\nMissing Values")
print((df == "?").sum())

# Observation:
# Missing values are stored as '?' instead of NaN.
# Therefore isnull() does not detect them.


# Q4. Detect outliers
plt.boxplot(df["age"])
plt.title("Box Plot of Age")
plt.ylabel("Age")
plt.show()

# Observation:
# The box plot shows the presence of outliers in the age attribute.



# Q5. Mean, Variance and Standard Deviation
mean = df["age"].mean()
variance = df["age"].var()
std = df["age"].std()

print("\nAge Statistics")
print("Mean :", mean)
print("Variance :", variance)
print("Standard Deviation :", std)

# Observation:
# Mean represents the average age.
# Variance and standard deviation indicate the spread of age values.