from sympy import pprint, Symbol, Function, diff, Eq, dsolve

x = Symbol('x')
f = Function('f')

print("f(x):")
pprint(f(x))

print("----------1----------")

print("diff(f(x)):")
pprint(diff(f(x)))
#or we can use f(x).diff(x) instead

print("----------2----------")

equation = Eq(diff(f(x)) - 2 * f(x), 5 * x)
print("equation:")
pprint(equation)

print("----------3----------")

#solve a differential equation
solution = dsolve(equation, f(x))
print("solution:")
pprint(solution)

"""
f(x):
f(x)
----------1----------
diff(f(x)):
d       
──(f(x))
dx      
----------2----------
equation:
          d             
-2⋅f(x) + ──(f(x)) = 5⋅x
          dx            
----------3----------
solution:
       ⎛                   -2⋅x⎞     
       ⎜     5⋅(-2⋅x - 1)⋅ℯ    ⎟  2⋅x
f(x) = ⎜C₁ + ──────────────────⎟⋅ℯ   
       ⎝             4         ⎠     
"""
