from sympy import diff, Symbol

x = Symbol('x')

f_of_x = x**3

print("f_of_x:", f_of_x)

#derivative of f with respect to x
df_dx = diff(f_of_x, x)

print("df_dx:", df_dx)


"""
f_of_x: x**3
df_dx: 3*x**2
"""
