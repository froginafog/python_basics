from sympy import diff, Symbol

x = Symbol('x')

f_of_x = x**3

print("f_of_x:", f_of_x)

#first derivative of f with respect to x
d1f_dx = diff(f_of_x, x, 1)

#second derivative of f with respect to x
d2f_dx = diff(f_of_x, x, 2)

#third derivative of f with respect to x
d3f_dx = diff(f_of_x, x, 3)

print("d1f_dx:", d1f_dx)
print("d2f_dx:", d2f_dx)
print("d3f_dx:", d3f_dx)

print("--------------------------------")

from sympy import Derivative  #for unevaluated derivative

#first derivative of f with respect to x
d1f_dx = Derivative(f_of_x, x, 1)

#second derivative of f with respect to x
d2f_dx = Derivative(f_of_x, x, 2)

#third derivative of f with respect to x
d3f_dx = Derivative(f_of_x, x, 3)

print("d1f_dx:", d1f_dx)
print("d2f_dx:", d2f_dx)
print("d3f_dx:", d3f_dx)
print()

d1f_dx = d1f_dx.doit() #do it, which means actually evaluate the derivative
d2f_dx = d2f_dx.doit()
d3f_dx = d3f_dx.doit()
print("d1f_dx:", d1f_dx)
print("d2f_dx:", d2f_dx)
print("d3f_dx:", d3f_dx)

"""
f_of_x: x**3
d1f_dx: 3*x**2
d2f_dx: 6*x
d3f_dx: 6
--------------------------------
d1f_dx: Derivative(x**3, x)
d2f_dx: Derivative(x**3, (x, 2))
d3f_dx: Derivative(x**3, (x, 3))

d1f_dx: 3*x**2
d2f_dx: 6*x
d3f_dx: 6
"""
