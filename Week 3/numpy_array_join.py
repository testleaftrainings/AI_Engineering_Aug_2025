import numpy as np
"""
#2D join
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print("One D Join")
array3 = np.concatenate((array1, array2))
print(array3)

#2D join
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print("Two D Join")
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)



arr = np.array([1, 6, 3, 6, 5, 7, 6, 6])

x = np.where(arr == 6)
y = np.where(arr%3 == 0)

print(x)
print(y)


#Sorting and Filter

array1 = np.array([1, 6, 3, 10, 5, 7, 2, 6])
x = np.sort(array1)
print(x)


arr2 = np.array([41, 42, 43, 44])

x = [True, True, True, True]

newarr = arr2[x]

print(newarr)
"""

arr1 = np.array([20,30,40,50])
arr2 = np.array([2,3,4,5])
newarr1 = np.add(arr1, arr2)
newarr2= np.subtract(arr1, arr2)
newarr3 = np.multiply(arr1, arr2)
newarr4 = np.divide(arr1, arr2)
print(newarr1)
print(newarr2)
print(newarr3)
print(newarr4)
