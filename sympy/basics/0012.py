from sympy.abc import x #for substitution
from sympy import sin, cos, pi 

f_of_x = sin(x) + cos(x)

print("f_of_x:", f_of_x)

result = f_of_x.subs(x, pi) #substitute pi into x

print("result:", result)

"""
f_of_x: sin(x) + cos(x)
result: -1
"""
