import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the CSV file into a DataFrame
file_path = r'C:\Users\Admin\Documents\Python\datasets\SalesData\SalesDataset.csv'
df = pd.read_csv(file_path)

# Display the first few rows
#print(df.head())

# Calculate 25th, 50th, and 75th percentiles for numeric columns
percentiles = df.describe(percentiles=[0.25, 0.5, 0.75])
print(percentiles)

p25 = df['Total Amount'].quantile(0.25)
p50 = df['Total Amount'].quantile(0.50)
p75 = df['Total Amount'].quantile(0.75)

print("25th Percentile of Total Amount :", p25)
print("50th Percentile of Total Amount :", p50)
print("75th Percentile of Total Amount :", p75)

# Calculate variance of the 'Total Amount' column
df['Total Amount'] = pd.to_numeric(df['Total Amount'], errors='coerce')
varianceTA = df['Total Amount'].var()
varianceQty = df['Quantity'].var()

print("Variance of TotalAmount:", varianceTA)
print("Variance of Quantity:", varianceQty)

group_variance=df.groupby('Product Category')['Total Amount'].var()

group_Gender_variance=df.groupby('Gender')['Total Amount'].var()

print("Grp Variance of TotalAmount:", group_variance)
print("Grp Variance of Quantity:", group_Gender_variance)
"""
plt.show()
group_variance.plot(kind='bar', color='orange', figsize=(10, 6))
plt.title('Variance of TotalAmount')
plt.ylabel('Variance')
plt.grid(True)
plt.show()
group_Gender_variance.plot(kind='bar', color='blue', figsize=(8, 6))
plt.title('Variance of TotalAmount')
plt.ylabel('Variance')
plt.grid(True)

plt.show()

"""