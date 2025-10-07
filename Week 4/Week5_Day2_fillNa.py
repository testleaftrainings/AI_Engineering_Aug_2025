#Replace missing values with some value (like mean, median, or custom).
import pandas as pd

data = {
    'Name': ['Alex', 'Ben', 'Cathy', 'David'],
    'Age': [25, None, 30, None],
    'Score': [85, 90, None, 70]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill missing Age with average age
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Fill missing Score with 0
df['Score'].fillna(0, inplace=True)

print("\nAfter fillna:")
print(df)
