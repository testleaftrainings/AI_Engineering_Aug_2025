#Relationship between Hours Studied and Marks.
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Hours_Studied': [2, 3, 4, 5, 6, 7, 8, 9],
    'Marks': [50, 55, 60, 65, 70, 75, 85, 90]
}
df = pd.DataFrame(data)

# Bivariate: Scatter plot
plt.scatter(df['Hours_Studied'], df['Marks'], color='blue')
plt.title("Bivariate Analysis - Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()
