from sympy import Matrix, pprint, linsolve, Symbol, Eq

"""
solve Ax = b

example

 1 * x_1 - 2 * x_2 + 3 * x_3 = 7
 2 * x_1 + 1 * x_2 + 1 * x_3 = 4
-3 * x_1 + 2 * x_2 - 2 * x_3 = -10
"""

x_1 = Symbol('x_1')
x_2 = Symbol('x_2')
x_3 = Symbol('x_3')

eq_1 = Eq(1 * x_1 - 2 * x_2 + 3 * x_3, 7)
eq_2 = Eq(2 * x_1 + 1 * x_2 + 1 * x_3, 4)
eq_3 = Eq(-3 * x_1 + 2 * x_2 - 2 * x_3, -10)

x = linsolve([eq_1, eq_2, eq_3], (x_1, x_2, x_3))
#x = {[x_1, x_2, x_3]}
#The type of x is <class 'sympy.sets.sets.FiniteSet'>

x = list(x) #convert to list

x = x[0] #the first set of the list is the solution that we want

print("x:")
pprint(x) 

print()

print("x_1:", x[0])
print("x_2:", x[1])
print("x_3:", x[2])


"""
x:
(2, -1, 1)

x_1: 2
x_2: -1
x_3: 1
"""
