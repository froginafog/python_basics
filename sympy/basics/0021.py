from sympy import Symbol, pi

r = Symbol('r')
f_of_r = pi * r**2
print("f_of_r:", f_of_r)
print("f_of_r.subs({r:3}):", f_of_r.subs({r:3})) #use this for exact result
print("f_of_r.evalf(subs = {r:3}):", f_of_r.evalf(subs = {r:3})) #use this for floating point (approximate) result

"""
f_of_r: pi*r**2
f_of_r.subs({r:3}): 9*pi
f_of_r.evalf(subs = {r:3}): 28.2743338823081
"""
