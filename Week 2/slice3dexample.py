import numpy as np
sample_3d = np.array([
    [[1, 2, 3], [5, 6, 7]],
    [[13, 14, 15], [17, 18, 19]],
    [[33, 44, 55], [77, 88, 99]]
])

print("3D Array:")
print(sample_3d)

# Slicing a specific "plane" 
slice_first_2d = sample_3d[0, :, :]
print("\n2D array (plane):")
print(slice_first_2d)

# Slicing a specific "row" across all planes
rowslice = sample_3d[:, 1, :]
print("\nSecond row in all planes:")
print(rowslice)

# Slicing a specific "column" across all planes
colslice = sample_3d[:, :, -1]
print("\nLast column in all planes:")
print(colslice)

#  Slicing a sub-section 
sub_section = sample_3d[0, 0, 0:2]
print("\nSub-section :")
#first plane, first row, first two columns
print(sub_section)