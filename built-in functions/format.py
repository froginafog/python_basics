"""
The format() function formats a specified value into a specified format.
Legal values:
'<' - Left aligns the result (within the available space)
'>' - Right aligns the result (within the available space)
'^' - Center aligns the result (within the available space)
'=' - Places the sign to the left most position
'+' - Use a plus sign to indicate if the result is positive or negative
'-' - Use a minus sign for negative values only
' ' - Use a leading space for positive numbers
',' - Use a comma as a thousand separator
'_' - Use a underscore as a thousand separator
'b' - Binary format
'c' - Converts the value into the corresponding unicode character
'd' - Decimal format
'e' - Scientific format, with a lower case e
'E' - Scientific format, with an upper case E
'f' - Fix point number format
'F' - Fix point number format, upper case
'g' - General format
'G' - General format (using a upper case E for scientific notations)
'o' - Octal format
'x' - Hex format, lower case
'X' - Hex format, upper case
'n' - Number format
'%' - Percentage format
"""

x = 1.23456
print("x:", x)
print("format(x, '%'):", format(x, '%'))

x = 123.456
print("x:", x)
print("format(x, 'e'):", format(x, 'e'))

n = 255
print("n:", n)
print("format(n, 'x'):", format(n, 'x'))

"""
x: 1.23456
format(x, '%'): 123.456000%
x: 123.456
format(x, 'e'): 1.234560e+02
n: 255
format(n, 'x'): ff
"""
