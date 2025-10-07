import numpy as np
import pandas as pd

s = pd.Series([20, 30, 40 ], index=['a','b','c'])
print(s)
print(s['b'])
print(s[0])

seriesdata = np.array(['t','e','s','t','l','e', 'a','f'])
print("From np array 1st location = ",seriesdata[4])
ser = pd.Series(seriesdata)
print("Series automatic indexing : \n", ser)

ser1 = pd.Series(seriesdata,index=[25,38,17,18,18,20,21,22])
#testleaf
#25 - t,38-e,17-s,18-t,18-l,20-e,21-a,22-f
#0 - t,1-e,2-s,3-t,4-l,5-e,6-a,7-f
#print("Series custom indexing : \n", ser1)
#print("Custom index at 10 the position =", ser1[20])

print("series ", ser[:4]) #test
print("series \n", ser[4::]) #Leaf

locvalue = ser1.loc[18:21]
print("locvalue =", locvalue)
ilocvalue = ser1.iloc[2:4]
print("ilocvalue =", ilocvalue)
