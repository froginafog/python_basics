#reversed() returns a reversed iterator object.

a = [1, 2, 3, 4, 5]
b = reversed(a) #here b is an iterator object
b = list(b) #here b becomes a list

print("a:", a)
print("b:", b)

"""
a: [1, 2, 3, 4, 5]
b: [5, 4, 3, 2, 1]
"""
