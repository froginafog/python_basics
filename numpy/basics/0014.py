import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
a = np.array(a)

num_rows = 3
num_columns = 4
matrix = a.reshape(num_rows, num_columns)

print(matrix) 

"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
"""
