import numpy as np

A = [
        [ 1, 2, 3],
        [ 2, 1, 2],
        [ 3, 2, 1]
    ]

inv_A = np.linalg.inv(A)  #inverse of A
print("inv_A:")
print(inv_A)

"""
inv_A:
[[-0.375  0.5    0.125]
 [ 0.5   -1.     0.5  ]
 [ 0.125  0.5   -0.375]]
"""

