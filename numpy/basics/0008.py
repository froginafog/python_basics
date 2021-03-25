import numpy as np

a = [1, 2, 3]
b = [1.1, 2.2, 3.3]
c = ["apple", "orange", "melon"]
a = np.array(a)
b = np.array(b)
c = np.array(c)

print("a.dtype:", a.dtype) 
print("b.dtype:", b.dtype)
print("c.dtype:", c.dtype) 

"""
a.dtype: int32
b.dtype: float64
c.dtype: <U6
"""
