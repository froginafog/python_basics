from numpy import random

a = [1, 2, 3, 4, 5]
print("a:", a)
random.shuffle(a)
print("shuffle a")
print("a:", a)

"""
a: [1, 2, 3, 4, 5]
shuffle a
a: [5, 2, 4, 3, 1]
"""
