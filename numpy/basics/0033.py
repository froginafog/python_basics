import numpy as np

a = [1, 2, 3, 4, 5, 6]

print("a:")
print(a)
print("--------------------------")

num_rows = 2
num_columns = 3
A = np.reshape(a, (num_rows, num_columns))

print("A:")
print(A)

"""
a:
[1, 2, 3, 4, 5, 6]
--------------------------
A:
[[1 2 3]
 [4 5 6]]
"""
