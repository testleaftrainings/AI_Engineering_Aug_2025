import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Generate a sample sales dataset
np.random.seed(42)
data = {
    'Sales': np.random.randint(100, 1000, 100),
    'Profit': np.random.randint(10, 300, 100),
    'Discount': np.random.uniform(0, 0.5, 100),
    'Quantity': np.random.randint(1, 10, 100)
}

df = pd.DataFrame(data)
print(df)
# Process the correlation matrix
correlation_matrix = df.corr()

print(correlation_matrix)

"""
# Create a heatmap of the correlation matrix
fig = px.imshow(correlation_matrix, text_auto=True, color_continuous_scale='Viridis',
                labels=dict(x="Features", y="Features", color="Correlation"),
                title="Correlation Matrix Heatmap for Sales Dataset")
"""





