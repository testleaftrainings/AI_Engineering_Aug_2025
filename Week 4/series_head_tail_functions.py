import numpy as np
import pandas as pd
seriesdata = np.array([4,6,8,2,1,3,4])
s = pd.Series(seriesdata)

print("From Series 4th location = ",seriesdata[4])
print("By default First 5 elements:")
print(s.head())
print("First 3 elements:")
threedata = s.head(3)
print(threedata)
print("By Excluding Last 4 elements:")
print(s.head(-4))
print("Last 4 elements using tail method:")
print(s.tail(4))

print(s.describe())

print(s.info())
