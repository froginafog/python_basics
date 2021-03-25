from sympy import pprint , Symbol, Derivative, Integral

x = Symbol('x')

f_of_x = x**2
print("f_of_x:")
pprint(f_of_x)

print("--------------------")

derivative_f_of_x = Derivative(f_of_x, x)
print("derivative_f_of_x:")
pprint(derivative_f_of_x)

print("--------------------")

integral_f_of_x = Integral(f_of_x, x)
print("integral_f_of_x:")
pprint(integral_f_of_x)

"""
f_of_x:
 2
x 
--------------------
derivative_f_of_x:
d ⎛ 2⎞
──⎝x ⎠
dx    
--------------------
integral_f_of_x:
⌠      
⎮  2   
⎮ x  dx
⌡      
"""
