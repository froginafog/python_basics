from sympy import Symbol

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

f_of_x_y_z = x**2 + y**2 + z**2

print("f_of_x_y_z:", f_of_x_y_z)

print("let x = 2, y = 3, z = 4")

result = f_of_x_y_z.subs({x: 2, y: 3, z: 4})

print("result:", result)

"""
f_of_x_y_z: x**2 + y**2 + z**2
let x = 2, y = 3, z = 4
result: 29
"""
