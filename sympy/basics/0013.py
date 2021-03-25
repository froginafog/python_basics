from sympy.abc import x, a, b #for substitution 

f_of_x = x**2

print("f_of_x:", f_of_x)

f_of_a_b = f_of_x.subs(x, a + b) #substitute a + b into x

print("f_of_a_b:", f_of_a_b)

f_of_a = f_of_a_b.subs(b, 3) #substitude 3 into b

print("f_of_a:", f_of_a)

result = f_of_a.subs(a, 2) #substitude 2 into a

print("result:", result)

"""
f_of_x: x**2
f_of_a_b: (a + b)**2
f_of_a: (a + 3)**2
result: 25
"""
