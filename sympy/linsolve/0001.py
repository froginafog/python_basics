from sympy import pprint, Symbol, Eq, linsolve

x = Symbol('x')
y = Symbol('y')

eq_1 = Eq(3 * x + 4 * y, 10)
eq_2 = Eq(2 * x - 5 * y, 6) 

print("eq_1:")
pprint(eq_1)

print("----------1---------")

print("eq_2:")
pprint(eq_2)

print("----------2---------")

#Since both equations are linear, we can use linsolve.

solution = linsolve([eq_1, eq_2], (x, y))
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
3⋅x + 4⋅y = 10
----------1---------
eq_2:
2⋅x - 5⋅y = 6
----------2---------
solution:
⎧⎛74      ⎞⎫
⎨⎜──, 2/23⎟⎬
⎩⎝23      ⎠⎭
----------3---------
solution:
⎡⎛74      ⎞⎤
⎢⎜──, 2/23⎟⎥
⎣⎝23      ⎠⎦
----------4---------
solution:
⎛74      ⎞
⎜──, 2/23⎟
⎝23      ⎠
----------5---------
x_solution:
74
──
23
----------6---------
y_solution:
2/23
"""
