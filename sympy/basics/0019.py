from sympy import Symbol, expand

x = Symbol('x')

f_of_x = (x + 1)*(x + 2)
print("f_of_x:", f_of_x)

f_of_x = expand(f_of_x)
print("f_of_x:", f_of_x)

"""
f_of_x: (x + 1)*(x + 2)
f_of_x: x**2 + 3*x + 2
"""
