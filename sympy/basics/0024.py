from sympy import Symbol, pprint, factorial

x = Symbol('x')

factorial_x = factorial(x)
result = factorial_x.subs({x: 5})
print("result:")
pprint(result)

"""
result:
120
"""
