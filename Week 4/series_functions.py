import numpy as np
import pandas as pd
s = pd.Series([20, 30, 40, 50, 20,50,20,None])
findvalues=[10,20]
d=pd.Series()
"""
print("Max:", s.max())
print("Min:", s.min())
print("Mean:", s.mean())
print("Count:", s.count())

d=s.drop_duplicates()
print(s)
print(d)

print("Unique values:", s.unique())
print("Number of Unique values:", s.nunique())
print("Value counts:\n", s.value_counts())
#print("Describe:\n", s.describe())
"""
print(s)
#print("Sorted : ", s.sort_values())
d=s.sort_values()
print(d)
#print("Sorted index : ", d.sort_index())
d=d.sort_index()
print(d)

#print(d.isin(findvalues))

#print(d)
#print("Dropped NAN values:\n", s.dropna()) # Removes missing (NaN) values from the Series.
#print("Series after filling NaN:\n", s.fillna(0))
#print(s)
