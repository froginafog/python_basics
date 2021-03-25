import numpy as np

a = [1, 2]
b = [3, 4]

a = np.array(a)
b = np.array(b)

print("a + b:", a + b) 
print("a * b:", a * b)
print("np.concatenate((a, b)):", np.concatenate((a, b)))

"""
a + b: [4 6]
a * b: [3 8]
np.concatenate((a, b)): [1 2 3 4]
"""
