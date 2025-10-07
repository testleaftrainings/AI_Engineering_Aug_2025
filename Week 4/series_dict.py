import pandas as pd
# Create dictionary
employee_experience = {
    'Santosh': 15,
    'Ram': 10,
    'Sita': 12,
    'Steve': 5
}

# Convert to Series
emp_series = pd.Series(employee_experience)
print(emp_series)
print("Experience of Ram is =", emp_series['Ram'])