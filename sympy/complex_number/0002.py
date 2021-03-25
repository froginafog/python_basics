from sympy import Symbol, pprint, I, re, im, Abs, conjugate, simplify

x1 = Symbol('x1')
y1 = Symbol('y1')
z1 = Symbol('z1')

x2 = Symbol('x2')
y2 = Symbol('y2')
z2 = Symbol('z2')

z1 = x1 + I*y1
z2 = x2 + I*y2

z1 = z1.subs({x1:2, y1:3})
z2 = z2.subs({x2:4, y2:5})

print("z1:")
pprint(z1)
print()

print("z2:")
pprint(z2)
print()

print("z1 + z2:")
pprint(z1 + z2)
print()

print("z1 - z2:")
pprint(z1 - z2)
print()

print("z1 * z2:")
pprint(z1 * z2)
print()

print("simplify(z1 * z2):")
pprint(simplify(z1 * z2))
print()

"""
z1:
2 + 3⋅ⅈ

z2:
4 + 5⋅ⅈ

z1 + z2:
6 + 8⋅ⅈ

z1 - z2:
-2 - 2⋅ⅈ

z1 * z2:
(2 + 3⋅ⅈ)⋅(4 + 5⋅ⅈ)

simplify(z1 * z2):
-7 + 22⋅ⅈ
"""
