import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the CSV file into a DataFrame
file_path = r'C:\Users\Admin\Documents\Python\datasets\SalesData\SalesDataset.csv'
write_file_path = r'C:\Users\Admin\Documents\Python\datasets\SalesData\total_amount_outliers.csv'
df = pd.read_csv(file_path)


# Load the dataset and fix headers
df = pd.read_csv(file_path, skiprows=1)
df.columns = ["Index", "Date", "Gender", "Age", "Product Category", "Quantity", "Price per Unit", "Total Amount"]

# Convert 'Total Amount' to numeric (in case of any formatting issues)
df["Total Amount"] = pd.to_numeric(df["Total Amount"], errors="coerce")

# Apply IQR method to detect outliers in 'Total Amount'
Q1 = df["Total Amount"].quantile(0.25)
Q3 = df["Total Amount"].quantile(0.75)
IQR = Q3 - Q1
print("Q1", Q1)
print("Q2", Q3)
print("IQR", IQR)
# Define outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(lower_bound)
print(upper_bound)

# Identify outliers
outliers = df[(df["Total Amount"] < lower_bound) | (df["Total Amount"] > upper_bound)]
print(outliers)
#df_cleaned = df[(df["Total Amount"] >= lower_bound) & (df["Total Amount"] <= upper_bound)]
# Save summary of outliers
outliers_summary = outliers[["Date", "Gender", "Age", "Product Category", "Total Amount"]]
print(outliers_summary)
outliers_summary.to_csv(write_file_path , index=False)

