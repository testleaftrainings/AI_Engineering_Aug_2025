#Check missing values in the DataFrame.
import pandas as pd

# Sample data with missing values
data = {
    'Name': ['Alex', 'Ben', 'Cathy', 'David'],
    'Age': [25, None, 30, None],
    'Score': [85, 90, None, 70]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Check for missing values
print("\nCheck with isnull():")
print(df.isnull())

# Count of missing values in each column
print("\nMissing values count:")
print(df.isnull().sum())
