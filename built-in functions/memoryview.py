#memoryview() returns a memory view object from a specified object.
x = memoryview(b"ABCDE")

print("x:", x)
print("x[0]:", x[0]) #print the unicode of the first character
print("x[1]:", x[1]) #print the unicode of the second character
print("x[2]:", x[2]) 
print("x[3]:", x[3])
print("x[4]:", x[4])

"""
x: <memory at 0x041D02C8>
x[0]: 65
x[1]: 66
x[2]: 67
x[3]: 68
x[4]: 69
"""
