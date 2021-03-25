import numpy as np

A = [[11, 12, 13, 14, 15],
     [21, 22, 23, 24, 25],
     [31, 32, 33, 34, 35]]

A = np.array(A)

print("A:")
print(A)
print("A.shape:", A.shape) #only worls for square matrices
A_num_rows = A.shape[0]
print("A_num_rows:", A_num_rows)
A_num_columns = A.shape[1]
print("A_num_columns:", A_num_columns)

print("--------------------------------")

B = [[11, 12, 13],
     [21, 22, 23, 24],
     [31, 32, 33, 34, 35]]

B = np.array(B)

print("B:")
print(B)
print("B.shape:", B.shape)
B_num_rows = B.shape[0]
print("B_num_rows:", B_num_rows)
B_num_columns = B.shape[1]
print("B_num_columns:", B_num_columns)

"""
a.shape: (3, 5)
number of rows in a: 3
number of columns in a: 5
"""
