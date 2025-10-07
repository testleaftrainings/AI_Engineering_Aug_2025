import numpy as np
import pandas as pd
s = pd.Series([20, 30, 50,20,None])
s1 = pd.Series([60, 70, None,10,0])
#findvalues=[10,20]
d=pd.Series()
print(s)
#print(s1)
#print("Dropped NAN values:\n", s.dropna()) # Removes missing (NaN) values from the Series.
#print("Series after filling NaN:\n", s.fillna(5))
#print(s.add(s1, fill_value=0))
print(s+s1)
#print(d)

