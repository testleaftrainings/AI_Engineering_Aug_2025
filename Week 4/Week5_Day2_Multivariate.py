#Hours Studied, Sleep Hours, and Marks.
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Hours_Studied': [2, 3, 4, 5, 6, 7, 8],
    'Sleep_Hours': [8, 7, 6, 7, 6, 5, 5],
    'Marks': [50, 55, 60, 65, 70, 80, 85]
}
df = pd.DataFrame(data)

# Multivariate: Use color and size to show 3rd variable
plt.scatter(df['Hours_Studied'], df['Marks'], 
            c=df['Sleep_Hours'], s=df['Sleep_Hours']*20, cmap='viridis')

plt.title("Multivariate Analysis - Hours, Sleep & Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.colorbar(label="Sleep Hours")  # shows scale of colors
plt.show()
