a = 1
b = 5
temp = 0 #temporary location

print("before switching:")
print("a:", a)
print("b:", b)

temp = a
a = b
b = temp

print("after switching:")
print("a:", a)
print("b:", b)

"""
before switching:
a: 1
b: 5
after switching:
a: 5
b: 1
"""
