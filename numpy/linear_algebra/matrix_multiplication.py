import numpy as np

A = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]
    ]

B = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

A = np.array(A)
B = np.array(B)

print("A * B:")
print(A * B)
    
"""
A * B:
[[ 11  24  39]
 [ 84 110 138]
 [217 256 297]]
"""
