import numpy as np

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

A = np.array(A)
B = np.array(B)

print("A:")
print(A)
print("------------------------")

print("B:")
print(B)
print("------------------------")

print("A + B:")
print(A + B)
print("------------------------")

print("A * B:")
print(A * B)
print("------------------------")

print("np.concatenate((A, B)):")
print(np.concatenate((A, B)))

print("------------------------")

print("np.concatenate((A, B), axis = 0):")
print(np.concatenate((A, B), axis = 0))

print("------------------------")

print("np.concatenate((A, B), axis = 1):")
print(np.concatenate((A, B), axis = 1))

print("------------------------")

print("np.concatenate((A, B), axis = None):")
print(np.concatenate((A, B), axis = None))



"""
A:
[[1 2]
 [3 4]]
------------------------
B:
[[5 6]
 [7 8]]
------------------------
A + B:
[[ 6  8]
 [10 12]]
------------------------
A * B:
[[ 5 12]
 [21 32]]
------------------------
np.concatenate((A, B)):
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
------------------------
np.concatenate((A, B), axis = 0):
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
------------------------
np.concatenate((A, B), axis = 1):
[[1 2 5 6]
 [3 4 7 8]]
------------------------
np.concatenate((A, B), axis = None):
[1 2 3 4 5 6 7 8]
"""
