# The any() function returns True if any item in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the any() function will return False.


a = [False, True, False] 
b = [False, False, False]
c = [0, 1, 0]
d = [0, 0, 0]

print("any(a):", any(a))
print("any(b):", any(b))
print("any(c):", any(c))
print("any(d):", any(d))

"""
any(a): True
any(b): False
any(c): True
any(d): False
"""
