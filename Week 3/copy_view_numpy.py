import numpy as np

samplearr = np.array([11, 12, 13, 14, 15])
"""
samplearr[0] = 44
x = samplearr.copy()
print(samplearr)
print(x)

"""
y = samplearr.view()
print("After View", y)
samplearr[0] = 44
y[0]=55
print("After modifying index samplearr ",samplearr)
#print(samplearr)
print("After modifying index y ",y)
