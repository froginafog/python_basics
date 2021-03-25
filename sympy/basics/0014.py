from sympy.abc import x, y, z #for substitution 

f_of_x_y_z = x**2 + y**2 + z**2

print("f_of_x_y_z:", f_of_x_y_z)

result = f_of_x_y_z.subs({x: 2, y:3, z:4})

print("result:", result)

"""
f_of_x_y_z: x**2 + y**2 + z**2
result: 29
"""
