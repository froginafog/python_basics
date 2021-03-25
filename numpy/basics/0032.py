import numpy as np

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

A = np.array(A)
B = np.array(B)

print("A:")
print(A)
print("------------------")

print("B:")
print(B)
print("------------------")

print("np.append(A, B):")
print(np.append(A, B)) #concatenates all the rows of A and B
print("------------------")

print("np.append(A, B, axis = 0):")
print(np.append(A, B, axis = 0))
print("------------------")

print("np.append(A, B, axis = 1):")
print(np.append(A, B, axis = 1))
print("------------------")

"""
A:
[[1 2]
 [3 4]]
------------------
B:
[[5 6]
 [7 8]]
------------------
np.append(A, B):
[1 2 3 4 5 6 7 8]
------------------
np.append(A, B, axis = 0):
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
------------------
np.append(A, B, axis = 1):
[[1 2 5 6]
 [3 4 7 8]]
------------------
"""
