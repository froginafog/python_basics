from sympy import diff, Symbol

x = Symbol('x')
y = Symbol('y')

f_of_x_y = x**3 + y**3 + x * y

print("f_of_x_y:", f_of_x_y)

df_dx = diff(f_of_x_y, x)

print("df_dx:", df_dx)

df_dy = diff(f_of_x_y, y)

print("df_dy:", df_dy)

"""
f_of_x_y: x**3 + x*y + y**3
df_dx: 3*x**2 + y
df_dy: x + 3*y**2
"""
