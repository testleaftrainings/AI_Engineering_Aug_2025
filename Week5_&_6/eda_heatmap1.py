import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset and fix headers
# Load the CSV file into a DataFrame
file_path = r'C:\Users\Admin\Documents\Python\datasets\SalesData\SalesDataset.csv'
df = pd.read_csv(file_path)
df.columns = ["Index", "Date", "Gender", "Age", "Product Category", "Quantity", "Price per Unit", "Total Amount"]


# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

# Filter for year 2023 only
df_2023 = df[df["Date"].dt.year == 2023]

# Extract day and month from the date
df_2023["Day"] = df_2023["Date"].dt.day
df_2023["Month"] = df_2023["Date"].dt.month

# Group by day and month and sum the total amount
heatmap_data = df_2023.groupby(["Day", "Month"])["Total Amount"].sum().reset_index()


print(heatmap_data)

# Pivot the data for heatmap
heatmap_pivot = heatmap_data.pivot(index="Day", columns="Month", values="Total Amount")

# Create heatmap using seaborn and matplotlib YlGnBu
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_pivot, annot=True, fmt=".0f", cmap="blues",cbar=True)

#sns.heatmap(heatmap_pivot, annot=True, fmt=".0f", cmap="YlOrRd")
plt.title("Heatmap of Total Amount by Date (Year 2023)")
plt.xlabel("Month")
plt.ylabel("Day")

plt.tight_layout()

# Save the heatmap
plt.savefig("date_total_amount_heatmap_matplotlib.png")
plt.show()