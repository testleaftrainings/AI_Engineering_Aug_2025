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

# Drop any row that contains at least one null value
df_dropped_rows = df.dropna()

print("DataFrame after dropping rows with any NA value:")
print(df_dropped_rows)

df_dropped_cols = df.dropna(how='any')

print("DataFrame after dropping columns with any NA value:")
print(df_dropped_cols)