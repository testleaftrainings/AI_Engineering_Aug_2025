#Remove rows (or columns) containing missing values.
import pandas as pd

data = {
    'Name': ['Alex', 'Ben', 'Cathy', 'David'],
    'Age': [25, None, 30, None],
    'Score': [85, 90, None, 70]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Drop rows with any missing values
df_drop = df.dropna()

print("\nAfter dropna (rows with NaN removed):")
print(df_drop)

# Drop columns with missing values
df_drop_col = df.dropna(axis=1)

print("\nAfter dropna (columns with NaN removed):")
print(df_drop_col)
