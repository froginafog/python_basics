from sympy import Symbol

x = Symbol('x')
y = Symbol('y')
f_of_x_y = x**2 + y**2
print("f_of_x_y:", f_of_x_y)
result = f_of_x_y.subs({x:2, y:3})
print("result:", result) #use this for exact result
result = result.evalf()
print("result:", result) #use this for floating point (approximate) result

"""
f_of_x_y: x**2 + y**2
result: 13
result: 13.0000000000000
"""
