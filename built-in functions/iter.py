# The iter() function returns an iterator object.

a = [1, 2, 3, 4, 5]
it = iter(a)

for i in range(0, len(a)):
    print(next(it), end = " ")

"""
1 2 3 4 5
"""
