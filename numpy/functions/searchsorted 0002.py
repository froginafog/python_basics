import numpy as np

a = [40, 50, 30, 10, 20]

print("a:", a)
print("sort a")

a = np.sort(a)
print("a:", a)

soughtValues = [40, 30, 20]
print("soughtValues:", soughtValues)
positions = np.searchsorted(a, soughtValues)
print("positions:", positions) 

"""
a: [40, 50, 30, 10, 20]
sort a
a: [10 20 30 40 50]
soughtValues: [40, 30, 20]
positions: [3 2 1]
"""
