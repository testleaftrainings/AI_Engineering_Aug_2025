import numpy as np

# Slicing [start:end:step]
# Slicing 2D array array[row_start:row_stop:row_step, col_start:col_stop:col_step]
OneDarr = np.array([1, 2, 3, 4, 5])

"""
twoD_arr = np.array([[1, 2, 3], [4, 5, 6]])
#threeD_arr = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]],[[1, 2, 3], [4, 5, 6],[7,8,9]])
threeD_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
"""
print(OneDarr)
print(OneDarr[1:3])
print(OneDarr[-1])
print(OneDarr[::-1])
print(OneDarr[3:])
"""
print(type(OneDarr))
#print(twoD_arr)

#print(threeD_arr)

#print(threeD_arr[1][1][2])

print(OneDarr.ndim)
print(twoD_arr.ndim)
print(threeD_arr.ndim)
"""