import numpy as np

#a numpy array has data of the same type

A = [[11, 12, 13],
     [21, 22, 22]
    ]

A = np.array(A)

print("dimensions of A:", A.shape)

num_rows = A.shape[0]
print("num_rows:", num_rows)

num_columns = A.shape[1]
print("num_columns:", num_columns)

"""
dimensions of A: (2, 3)
num_rows: 2
num_columns: 3
"""
