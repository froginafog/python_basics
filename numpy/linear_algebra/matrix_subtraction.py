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

print("A - B:")
print(A - B)
    
"""
A - B:
[[10 10 10]
 [17 17 17]
 [24 24 24]]
"""
