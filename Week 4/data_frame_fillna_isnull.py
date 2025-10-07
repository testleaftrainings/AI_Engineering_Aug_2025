import numpy as np
import pandas as pd

dict = {'1st Round':[100, 90, None, 95],
        '2nd Round': [30, 45, 56, None],
        '3rd Round':[None, 40, 80, 98]}
df = pd.DataFrame(dict)
#print(df.isnull())
#df=df.dropna()
#df=df.fillna(10)
print(df)
#print(df.isnull())
print(df.loc[[2,1]])
print(df.iloc[1])

