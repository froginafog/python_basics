import numpy as np

a = [1, 2, 3, 4, 5]
a = np.array(a)
b = a.copy()
#changes made to "a" does not affect "b"

print("a:", a)
print("b:", b)

print("---------------")
for i in range(0, len(a)):
    a[i] = 0

print("a:", a)
print("b:", b)

"""
a: [1 2 3 4 5]
b: [1 2 3 4 5]
---------------
a: [0 0 0 0 0]
b: [1 2 3 4 5]
