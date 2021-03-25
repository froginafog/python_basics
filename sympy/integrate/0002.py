from sympy import integrate, Symbol

x = Symbol('x')

f_of_x = x**2 

print("f_of_x:", f_of_x)

lower_limit = 0
upper_limit = 2
result = integrate(f_of_x, (x, lower_limit, upper_limit))

print("result:", result)

"""
f_of_x: x**2
result: 8/3
"""
