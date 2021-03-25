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

print("---------------------------")

num_rows = A.shape[0]
num_columns = A.shape[1]

print("A:")

for i in range(0, num_rows):
    for j in range(0, num_columns):
        print(A[i][j], end = " ")
    print()

"""
A:
[[11 12 13]
 [21 22 23]
 [31 32 33]]
---------------------------
A:
11 12 13 
21 22 23 
31 32 33 
"""
