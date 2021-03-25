from sympy import pprint, Symbol, Eq, sin, cos

x = Symbol('x')

lhs = x**2 + 2*x + 1
print("lhs:")
pprint(lhs)

print("--------------------")

rhs = sin(x) + cos(x)
print("rhs:")
pprint(rhs)

print("--------------------")

equation = Eq(lhs, rhs)

pprint(equation)

"""
lhs:
 2          
x  + 2⋅x + 1
--------------------
rhs:
sin(x) + cos(x)
--------------------
 2                            
x  + 2⋅x + 1 = sin(x) + cos(x)
"""
