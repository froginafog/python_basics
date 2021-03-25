from sympy import integrate, Symbol, exp, oo
#oo for infinity

x = Symbol('x')

f_of_x = exp(-x)

print("f_of_x:", f_of_x)

lower_limit = 0
upper_limit = oo
result = integrate(f_of_x, (x, lower_limit, upper_limit))

print("result:", result)

"""
f_of_x: exp(-x)
result: 1
"""
