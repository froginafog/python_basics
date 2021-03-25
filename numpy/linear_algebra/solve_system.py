import numpy as np

"""
solve Ax = b

example

 1 * x_1 - 2 * x_2 + 3 * x_3 = 7
 2 * x_1 + 1 * x_2 + 1 * x_3 = 4
-3 * x_1 + 2 * x_2 - 2 * x_3 = -10
"""

A = [
        [ 1, -2,  3],
        [ 2,  1,  1],
        [-3,  2, -2]
    ]

b = [7, 4, -10]

#x = [x_1, x_2, x_3]

x = np.linalg.solve(A, b)
print("x:")
print(x)

"""
x:
[ 2. -1.  1.]
"""

