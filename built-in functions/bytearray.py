# The bytearray() function returns a bytearray object.
# It can convert objects into bytearray objects,
# or create empty bytearray object of the specified size.

for n in range(0, 10):
    print("bytearray(" + str(n) + "):", bytearray(n))
    
"""
bytearray(0): bytearray(b'')
bytearray(1): bytearray(b'\x00')
bytearray(2): bytearray(b'\x00\x00')
bytearray(3): bytearray(b'\x00\x00\x00')
bytearray(4): bytearray(b'\x00\x00\x00\x00')
bytearray(5): bytearray(b'\x00\x00\x00\x00\x00')
bytearray(6): bytearray(b'\x00\x00\x00\x00\x00\x00')
bytearray(7): bytearray(b'\x00\x00\x00\x00\x00\x00\x00')
bytearray(8): bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00')
bytearray(9): bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00')
"""
