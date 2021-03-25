from sympy import simplify, sin, cos, Symbol

r = Symbol('r')
f_of_r = r * sin(r)**2 + r * cos(r)**2
print("f_of_r:", f_of_r)
f_of_r = simplify(f_of_r) 
print("f_of_r:", f_of_r)

#f_of_r = r * sin(r)**2 + r * cos(r)**2
#       = r * sin(r)**2 + r * cos(r)**2
#       = r * (sin(r)**2 + cos(r)**2)
#       = r * 1
#       = r

"""
f_of_r: r*sin(r)**2 + r*cos(r)**2
f_of_r: r
"""
