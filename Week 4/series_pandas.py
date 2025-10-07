import numpy as np
import pandas as pd;
a = [1, 7, 2]
serieslist = pd.Series(a)
print(serieslist)

serieslist2 = pd.Series(a, index = ["x", "y", "z"])
print(serieslist2)