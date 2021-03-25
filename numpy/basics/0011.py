import numpy as np

a = np.array([1, 2, 3, 4, 5])

b = a.view()
#let "b" point to "a"
#changing "a" affects "b"
#changing "b" affects "a" 

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
b: [0 0 0 0 0]
"""
