from sympy import Symbol, lambdify

x = Symbol('x')
y = Symbol('y')

f_of_x_y = x**2 + y**2

f = lambdify([x, y], f_of_x_y)
#convert a sympy expression into a function

print("f(2,3):", f(2,3))

"""
f(2,3): 13
"""
