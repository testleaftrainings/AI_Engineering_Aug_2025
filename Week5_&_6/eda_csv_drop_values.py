import pandas as pd
# Create a sample CSV file for our example

csv_data = """id,name,score,major
101,Arun,88,Physics
102,Bala,,Math
103,Charles,95,
104,David,76,Chemistry
105,Edward,NaN,Biology
"""


with open("student_data.csv", "w") as f:
    f.write(csv_data)
    

# Read the CSV file into a pandas DataFrame
students_df = pd.read_csv("student_data.csv")

print("--- Original DataFrame from CSV ---")
print(students_df)

print("describe")
print(students_df['score'].describe())

# Check for null/NA values in the new DataFrame
print("\n--- Checking for NA values ---")
print(students_df.isna().sum())

# Process the data: Let's drop rows with any missing values
processed_df = students_df.dropna()

print("\n--- DataFrame after dropping rows with missing values ---")
print(processed_df)

# You could also fill missing values instead of dropping them
# For example, fill missing scores with 0 and missing majors with 'Undeclared'
filled_df = students_df.fillna({'score': 0, 'major': 'Undeclared'})

print("\n--- DataFrame after filling missing values ---")
print(filled_df)