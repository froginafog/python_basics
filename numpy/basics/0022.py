import numpy as np

a = [[11, 12, 13, 14, 15],
     [21, 22, 23, 24, 25]]
a = np.array(a)
print("a:")
print(a)

print("type(a):", type(a))

print("number of dimensions:", a.ndim)

print("shape of the array:", a.shape)
print("number of rows in the array:", a.shape[0])
print("number of columns in the array:", a.shape[1])

print("size of the array:", a.size)

print("type of the elements in the array:", a.dtype)

"""
a:
[[11 12 13 14 15]
 [21 22 23 24 25]]
type(a): <class 'numpy.ndarray'>
number of dimensions: 2
shape of the array: (2, 5)
number of rows in the array: 2
number of columns in the array: 5
size of the array: 10
type of the elements in the array: int32
"""
