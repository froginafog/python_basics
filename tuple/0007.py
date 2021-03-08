a = (3, 2, 1, 5, 4)
#the elements of a tuple cannot be changed
#but we can convert it into a list to change the values
#and then convert it back to a tuple

a = list(a)

a[2] = 10

a = tuple(a)

print("a:", a)

"""
a: (3, 2, 10, 5, 4)
"""
