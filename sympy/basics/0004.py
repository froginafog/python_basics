from sympy import Float

#scientific notation
x = 123.456
print("x:", x)
print("Float(str(x) + 'E-2'):", Float(str(x) + 'E-2'))  #123.456 * 10^-2
print("Float(str(x) + 'E-1'):", Float(str(x) + 'E-1'))  #123.456 * 10^-1
print("Float(str(x) + 'E0'):", Float(str(x) + 'E0'))    #123.456 * 10^0
print("Float(str(x) + 'E1'):", Float(str(x) + 'E1'))    #123.456 * 10^1
print("Float(str(x) + 'E2'):", Float(str(x) + 'E2'))    #123.456 * 10^2

"""
x: 123.456
Float(str(x) + 'E-2'): 1.23456000000000
Float(str(x) + 'E-1'): 12.3456000000000
Float(str(x) + 'E0'): 123.456000000000
Float(str(x) + 'E1'): 1234.56000000000
Float(str(x) + 'E2'): 12345.6000000000
"""
