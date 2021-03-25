from sympy import integrate, Symbol

x = Symbol('x')

f_of_x = x**2 

print("f_of_x:", f_of_x)

interal_f_of_x = integrate(f_of_x, x)

print("interal_f_of_x:", interal_f_of_x)

"""
f_of_x: x**2
interal_f_of_x: x**3/3
"""
