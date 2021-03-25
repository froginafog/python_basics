from sympy import Symbol, pprint, I, re, im, Abs, conjugate

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

z = x + I*y

z = z.subs({x:2, y:3})

print("z:")
pprint(z)

print("re(z):")
pprint(re(z))

print("im(z):")
pprint(im(z))

print("Abs(z):")
pprint(Abs(z))

print("conjugate(z):")
pprint(conjugate(z))

print("z + conjugate(z):")
pprint(z + conjugate(z))

"""
z:
2 + 3⋅ⅈ
re(z):
2
im(z):
3
Abs(z):
√13
conjugate(z):
2 - 3⋅ⅈ
z + conjugate(z):
4
"""
