import numpy as np

rows = 2
columns = 5

a = np.zeros((rows, columns)) #create a 2D array of zeros (floats)
print("a:")
print(a)
print("------------------------")

a = a.astype(int) #convert "a" to an array of integers

print("a:")
print(a)

"""
a:
a:
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
------------------------
a:
[[0 0 0 0 0]
 [0 0 0 0 0]]
"""
