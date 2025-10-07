import numpy as np
"""
arr1 = np.array([[11, 12, 13, 14], [15, 16, 17, 18]])
print("Shaping Dimension is =",arr1.ndim)
print("Shape is =", arr1.shape)
"""

arr_sample = np.array([1,2,3,4,5,6,7,8,9,10,1,12])
print("Before reshaping  Dimension is =", arr_sample.ndim)
newarr = arr_sample.reshape(4,3)
print("New reshaped Array is =", newarr)
print("After reshaping  Dimension is =", newarr.ndim)

"""
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)
"""
