import numpy as np

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12]]
A = np.array(A)

#split "A" into an array of 2 matrices (2D arrays)
A_split_into_2 = np.array_split(A, 2) 

print("A:")
print(A)
print("-------------------------")
print("A_split_into_2:")
print(A_split_into_2)
print("-------------------------")
print("A_split_into_2[0]:")
print(A_split_into_2[0])
print("-------------------------")
print("A_split_into_2[1]:")
print(A_split_into_2[1])

"""
A:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
-------------------------
A_split_into_2:
[array([[1, 2, 3],
       [4, 5, 6]]), array([[ 7,  8,  9],
       [10, 11, 12]])]
-------------------------
A_split_into_2[0]:
[[1 2 3]
 [4 5 6]]
-------------------------
A_split_into_2[1]:
[[ 7  8  9]
 [10 11 12]]
"""
