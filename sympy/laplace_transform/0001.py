from sympy import Symbol, laplace_transform

t = Symbol('t')
s = Symbol('s')

f_of_t = t**3

#laplace transform of t^n is equal to n!/s^(n+1)

print("f_of_t:", f_of_t)

laplace_transform_f_of_x = laplace_transform(f_of_t, t, s)

print("laplace_transform_f_of_x:", laplace_transform_f_of_x)

"""
f_of_t: t**3
laplace_transform_f_of_x: (6/s**4, 0, True)
"""
