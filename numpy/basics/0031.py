import numpy as np

a = [1, 2]

b = [3, 4]

a = np.array(a)
b = np.array(b)


print("a:", a)
print("b:", b)
print("np.append(a, b):", np.append(a, b)) #append 'b' to the end of 'a'

"""
a: [1 2]
b: [3 4]
np.append(a, b): [1 2 3 4]
"""
