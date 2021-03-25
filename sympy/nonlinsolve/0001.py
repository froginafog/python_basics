from sympy import pprint, Symbol, Eq, nonlinsolve

x = Symbol('x')
y = Symbol('y')

eq_1 = Eq(x**2 + y, 0)
eq_2 = Eq(x - y, 2) 

print("eq_1:")
pprint(eq_1)

print("----------1---------")

print("eq_2:")
pprint(eq_2)

print("----------2---------")

#Since one of the equations is nonlinear, we should use nonlinsolve.

solution = nonlinsolve([eq_1, eq_2], (x, y))
#The type of solution is <class 'sympy.sets.sets.FiniteSet'>
print("solution:")
pprint(solution)

print("----------3---------")

solution = list(solution) #convert the solution into a list
print("solution:")
pprint(solution)

print("----------4---------")

solution = solution[0]
#The type of solution is <class 'sympy.core.containers.Tuple'>
print("solution:")
pprint(solution)

print("----------5---------")

x_solution = solution[0]
#The first element of the tuple is the x-solution.
print("x_solution:")
pprint(x_solution)

print("----------6---------")

y_solution = solution[1]
#The second element of the tuple is the y-solution.
print("y_solution:")
pprint(y_solution)

"""
eq_1:
 2        
x  + y = 0
----------1---------
eq_2:
x - y = 2
----------2---------
solution:
{(-2, -4), (1, -1)}
----------3---------
solution:
[(-2, -4), (1, -1)]
----------4---------
solution:
(-2, -4)
----------5---------
x_solution:
-2
----------6---------
y_solution:
-4
"""
