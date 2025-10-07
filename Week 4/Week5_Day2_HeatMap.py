import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Math': [80, 90, 70, 60, np.nan],
    'Science': [85, 95, 75, 65, 70],
    'English': [78, np.nan, 72, 68, 80],
    'History': [88, 92, np.nan, 70, 75]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Step 1: Fill missing values with column average
df_filled = df.fillna(df.mean())

print("\nAfter filling NaN with column mean:")
print(df_filled)

# Step 2: Correlation matrix
corr = df_filled.corr()
print("\nCorrelation Matrix:")
print(corr)

# Step 3: Plot heatmap using matplotlib
plt.imshow(corr, cmap='coolwarm', interpolation='nearest')
plt.colorbar()

# Add column labels
plt.xticks(range(len(corr)), list(corr.columns), rotation=45)
plt.yticks(range(len(corr)), list(corr.columns))

plt.title("Heatmap of Subject Scores", fontsize=14)
plt.show()
