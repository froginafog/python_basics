from sympy import pprint, Symbol, Eq, solveset

x = Symbol('x')

lhs = x**2 + 2*x + 1
print("lhs:")
pprint(lhs)

print("--------------------")

rhs = 5
print("rhs:")
pprint(rhs)

print("--------------------")

print("equation:")
equation = Eq(lhs, rhs)

pprint(equation)

print("--------------------")

solution = solveset(equation, x)
#The type of solution is <class 'sympy.sets.sets.FiniteSet'>
solution = list(solution) #convert to list
print("solution:")
print(solution)
print()
print("x1:")
pprint(solution[0])
print("x2:")
pprint(solution[1])

"""
lhs:
 2          
x  + 2⋅x + 1
--------------------
rhs:
5
--------------------
equation:
 2              
x  + 2⋅x + 1 = 5
--------------------
solution:
[-1 + sqrt(5), -sqrt(5) - 1]

x1:
-1 + √5
x2:
-√5 - 1
"""
