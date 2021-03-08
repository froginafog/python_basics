# The bool() function returns the boolean value of a specified object.
# The object will always return True, unless:
# The object is empty, like [], (), {}
# The object is False
# The object is 0
# The object is None

print("bool([]):", bool([]))
print("bool(False):", bool(False))
print("bool(0):", bool(0))
print("bool(None):", bool(None))
print("bool(-1):", bool(-1))
print("bool(-2):", bool(-2))
print("bool(1):", bool(1))
print("bool(2):", bool(2))

"""
bool([]): False
bool(False): False
bool(0): False
bool(None): False
bool(-1): True
bool(-2): True
bool(1): True
bool(2): True
"""
