import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values (np.nan)
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12],
    'D': [np.nan, 14, 15, 16]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Check for null values
print("\nChecking for null values with isnull():")
print(df.isnull())

# To get a count of nulls in each column
print("\nCount of null values per column:")
print(df.isnull().sum())
"""
print("isna")
# Using isna() - it gives the exact same result as isnull()
print("Checking for NA values with isna():")
print(df.isna())

# Getting the count of NA values per column
print("\nCount of NA values per column:")
print(df.isna().sum())
"""