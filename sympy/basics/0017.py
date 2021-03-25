from sympy import Symbol

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

f_of_x_y_z = x**2 + y**2 + z**2

print("f_of_x_y_z:", f_of_x_y_z)

print("let x = a + b, y = a + c, z = b + c")

f_of_a_b_c = f_of_x_y_z.subs({x: a + b, y: a + c, z: b + c})

print("f_of_a_b_c:", f_of_a_b_c)

print("let a = 2, b = 3, c = 4")

result = f_of_a_b_c.subs({a: 2, b: 3, c: 4})

print("result:", result)

"""
f_of_x_y_z: x**2 + y**2 + z**2
let x = a + b, y = a + c, z = b + c
f_of_a_b_c: (a + b)**2 + (a + c)**2 + (b + c)**2
let a = 2, b = 3, c = 4
result: 110
"""
