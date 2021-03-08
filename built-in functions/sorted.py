# The sorted() function returns a sorted list of the specified iterable object.
a = [4, 2, 7, 6, 8, 9, 3, 0, 1, 5]

a = sorted(a)

print("a:", a)

a = sorted(a, reverse = True)

print("a:", a)

"""
a: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""
