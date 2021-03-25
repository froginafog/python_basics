from sympy import diff, Symbol, sin

x = Symbol('x')

f_of_x = sin(x) + x**2

print("f_of_x:", f_of_x)

#derivative of f with respect to x
df_dx = diff(f_of_x, x)

print("df_dx:", df_dx)


"""
f_of_x: x**2 + sin(x)
df_dx: 2*x + cos(x)
"""
