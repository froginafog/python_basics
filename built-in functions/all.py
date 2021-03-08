# The all() function returns True if all items in an iterable are true,
# otherwise it returns False.

a = [True, True, False] 
b = [True, True, True]
c = [0, 1, 0, 1]
d = [1, 1, 1, 1]

print("all(a):", all(a))
print("all(b):", all(b))
print("all(c):", all(c))
print("all(d):", all(d))

"""
all(a): False
all(b): True
all(c): False
all(d): True
"""
