# The int() function converts a value into an integer.

x = 123.456
integerPart = int(x)
fractionalPart = x - integerPart
print(str(x) + " = " + str(integerPart) + " + " + str(fractionalPart)) 
fractionalPart = format(fractionalPart, '.3f')
print(str(x) + " = " + str(integerPart) + " + " + str(fractionalPart)) 

"""
123.456 = 123 + 0.45600000000000307
123.456 = 123 + 0.456
"""
