#Distribution of marks in a class.
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Marks': [45, 67, 89, 56, 90, 76, 65, 88, 92, 70]}
df = pd.DataFrame(data)

# Univariate: Histogram of Marks
plt.hist(df['Marks'], bins=5, edgecolor='black')
plt.title("Univariate Analysis - Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
