from sympy import Symbol, pi

r = Symbol('r')
f_of_r = pi * r**2 + sin(pi*r)
print("f_of_r:", f_of_r)
result = f_of_r.subs({r:3})
print("result:", result) #use this for exact result
result = result.evalf()
print("result:", result) #use this for floating point (approximate) result

"""
f_of_r: pi*r**2
result: 9*pi
result: 28.2743338823081
"""
