import pandas as pd

# Create a sample DataFrame
data = {
    'Category': ['AI', 'Pandas', 'AI', 'EDA', 'Pandas', 'AI', 'EDA'],
    'Cohort1': [10, 15, 12, 8, 20, 11, 9],
    'Cohort2': [5, 7, 6, 4, 8, 5, 4]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Group by 'Category' and calculate the sum and mean of 'Value1'
# and the sum of 'Value2' for each category
grouped_df = df.groupby('Category').agg(
    Total_Cohort1=('Cohort1', 'sum'),
    Mean_Cohort1=('Cohort1', 'mean'),
    Total_Cohort2=('Cohort2', 'sum')
)

print("\nGrouped and Aggregated DataFrame:")
print(grouped_df)
tempdf=grouped_df
print(tempdf.loc['AI'])
