from sympy import Float

print("Float(3):", Float(3))

print("Float(123.456, 0):", Float(123.456, 0)) #keep 0 digit 
print("Float(123.456, 1):", Float(123.456, 1)) #keep 1 digit
print("Float(123.456, 2):", Float(123.456, 2)) #keep 2 digits
print("Float(123.456, 3):", Float(123.456, 3)) #keep 3 digits
print("Float(123.456, 4):", Float(123.456, 4)) #keep 4 digits
print("Float(123.456, 5):", Float(123.456, 5)) #keep 5 digits
print("Float(123.456, 6):", Float(123.456, 6)) #keep 6 digits
print("Float(123.456, 7):", Float(123.456, 7)) #keep 7 digits

"""
Float(3): 3.00000000000000
Float(123.456, 0): 0.e+2
Float(123.456, 1): 1.e+2
Float(123.456, 2): 1.2e+2
Float(123.456, 3): 123.
Float(123.456, 4): 123.5
Float(123.456, 5): 123.46
Float(123.456, 6): 123.456
Float(123.456, 7): 123.4560
"""
