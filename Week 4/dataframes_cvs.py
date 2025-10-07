import pandas as pd

# Create a sample CSV file for demonstration
empdata = {'Name': ['Alex', 'Steve', 'Charles'],
        'Experience': [20, 15, 10],
        'Location': ['Bangalore', 'Chennai', 'Delhi']}
emp_df = pd.DataFrame(empdata)
print(emp_df)
emp_df.to_csv('emp_input.csv', index=True) # Save withsout the DataFrame index

# Create a new DataFrame with data to append
new_data = {'Name': ['Ram', 'Sita'], 'Experience': [15, 20],  'Location': ['Bangalore', 'Chennai']}
df_new = pd.DataFrame(new_data)

# Append the new data to the existing CSV
df_new.to_csv('emp_input.csv', mode='a', header=False, index=False)


print("Reading only two columns")
# Read the CSV file into a DataFrame
df = pd.read_csv('emp_input.csv',usecols=['Name', 'Location'])

# Display the DataFrame
print("DataFrame read from CSV:")
print(df)
print("Printing First 2")
print(df.head(2))
print("Extracting only Alex")
print(df[df['Name']=='Alex'])