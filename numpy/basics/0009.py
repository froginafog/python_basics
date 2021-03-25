import numpy as np

a = [1.1, 2.2, 3.3]
#we can't apply 'a.dtype' yet
#we first have to convert the list to an array using numpy

a = np.array(a)
a = a.astype(int) #convert "a" to an array of "int"
print("a:", a)
print("a.dtype:", a.dtype)

"""
a: [1 2 3]
a.dtype: int32
"""
