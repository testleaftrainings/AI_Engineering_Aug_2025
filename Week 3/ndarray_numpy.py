import numpy as np
a=5
OneDarr = np.array([1, 2, 3, 4, 5])
twoD_arr = np.array([[1, 2, 3], [4, 5, 6]])
#threeD_arr = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]],[[1, 2, 3], [4, 5, 6],[7,8,9]])
threeD_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[11,12, 13], [14, 15, 16]]])
"""
print(OneDarr[0]) #1
print(OneDarr[3]) #4
print(OneDarr)

#print(OneDarr[1:3])
print(type(a))
print(type(OneDarr))

print(twoD_arr[0][1]) #2
print(twoD_arr[1][2]) #6
print(twoD_arr)
"""
print(threeD_arr)

print("Value of specific Location [1][0][1] is =", threeD_arr[1][0][1])

#print(threeD_arr[1][1][2])
"""
print(OneDarr.ndim)
print(twoD_arr.ndim)
"""
print(threeD_arr.ndim)