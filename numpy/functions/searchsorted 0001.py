import numpy as np

a = [40, 50, 30, 10, 20]

print("a:", a)
print("sort a")

a = np.sort(a)
print("a:", a)

soughtValue = 30
position = np.searchsorted(a, soughtValue)
#searchsorted is a binary search, so the array must be sorted before usage

print("position:", position) 

"""
a: [40, 50, 30, 10, 22]
sort a
a: [10 22 30 40 50]
position: 2
"""
