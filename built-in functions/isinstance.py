"""
The isinstance() function returns True if the specified
object is of the specified type
Otherwise, it returns False.
If the type parameter is a tuple, this function will
return True if the object is one of the types in the tuple.
"""


print("isinstance(5, int):", isinstance(5, int))
print("isinstance(5.5, float):", isinstance(5.5, float))
print("isinstance(5.5, int):", isinstance(5.5, int))
print("isinstance(5, str):", isinstance(5, str))
print("isinstance(\"hello\", str):", isinstance("hello", str))

print("------------------------")
print("Enter an integer, a floating point number, or a string:", end = " ")
x = input() # x is a string by default
x = int(x)

if isinstance(x, int):
    print("%d is an integer" %(x))

if isinstance(x, float):
    print("%d is an integer" %(x))

"""
isinstance(5, int): True
isinstance(5.5, float): True
isinstance(5.5, int): False
isinstance(5, str): False
isinstance("hello", str): True
"""
