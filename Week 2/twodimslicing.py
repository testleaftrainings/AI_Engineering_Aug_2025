# Showcasing two dimensional array - Slicing
import numpy as np
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(matrix)

"""
second_row = matrix[1,:]
print("second_row is =", second_row)

third_column = matrix[:, 2]
print("Third Column is =",third_column)

sub_matrix = matrix[:2, 1:3]
print("sub matrix is \n", sub_matrix)

"""









# Selects all elements in the second row (index 1)
# Output: [5 6 7 8]

# Selects all elements in the third column (index 2)
# Output: [ 3  7 11]
# Selects the first two rows and columns from index 1 to 2 (exclusive)
# Output: [[2 3]
#          [6 7]]
    