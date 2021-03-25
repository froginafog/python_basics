import numpy as np

#a numpy array has data of the same type

a = [10, 20, 30]
print("convert a list into an numpy array of type int16")
a = np.array(a, dtype = 'int16')
print("a:", a[:])
print("number of elements in a:", a.size)
print("number of bytes occupied by each element of array a:", a.itemsize)
print("number of bytes occupied by a:", a.nbytes) 

print("-----------------------------------------------------------------------")

print("increase the size of array a to int32")
a = np.array(a, dtype = 'int32')
print("a:", a[:])
print("number of elements in a:", a.size)
print("number of bytes occupied by each element of array a:", a.itemsize)
print("number of bytes occupied by a:", a.nbytes) 

print("-----------------------------------------------------------------------")

print("convert the array of integers to an array of floats")
a = np.array(a, dtype = 'float')
print("a:", a[:])
print("number of elements in a:", a.size)
print("number of bytes occupied by each element of array a:", a.itemsize)
print("number of bytes occupied by a:", a.nbytes) 
      
"""
convert a list into an numpy array of type int16
a: [10 20 30]
number of elements in a: 3
number of bytes occupied by each element of array a: 2
number of bytes occupied by a: 6
-----------------------------------------------------------------------
increase the size of array a to int32
a: [10 20 30]
number of elements in a: 3
number of bytes occupied by each element of array a: 4
number of bytes occupied by a: 12
-----------------------------------------------------------------------
convert the array of integers to an array of floats
a: [10. 20. 30.]
number of elements in a: 3
number of bytes occupied by each element of array a: 8
number of bytes occupied by a: 24
"""
