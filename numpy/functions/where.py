import numpy as np

a = np.array([1, 3, 3, 2, 5, 5, 6, 5])

positions = np.where(a == 5)

print("positions of the value 5 in the array:", positions) 

"""
positions of the value 5 in the array: (array([4, 5, 7], dtype=int32),)
"""
