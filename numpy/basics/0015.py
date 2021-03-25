import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

a_plus_b = a + b
a_concatenate_b = np.concatenate((a, b))

print("a_plus_b:", a_plus_b)
print("a_concatenate_b:", a_concatenate_b)

"""
a_plus_b: [5 7 9]
a_concatenate_b: [1 2 3 4 5 6]
"""
