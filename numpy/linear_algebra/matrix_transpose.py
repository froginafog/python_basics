import numpy as np

A = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]
    ]
#A is a list

#convert A into a numpy array
A = np.array(A)

print("A:")
print(A)

print("------------------------")

A_T = A.T #transpose of A
print("A_T:")
print(A_T) 


"""
A:
[[11 12 13]
 [21 22 23]
 [31 32 33]]
------------------------
A_T:
[[11 21 31]
 [12 22 32]
 [13 23 33]]
"""
