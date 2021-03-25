from sympy import Matrix, pprint, linsolve

"""
solve Ax = b

example

 1 * x_1 - 2 * x_2 + 3 * x_3 = 7
 2 * x_1 + 1 * x_2 + 1 * x_3 = 4
-3 * x_1 + 2 * x_2 - 2 * x_3 = -10
"""

A = [
        [ 1, -2,  3],
        [ 2,  1,  1],
        [-3,  2, -2]
    ]

A = Matrix(A)

b = [7, 4, -10]
b = Matrix(b)
x = linsolve([A, b])
print("x:")
pprint(x) 

print("--------------------")

x = list(x) #convert to list

print("x:")
pprint(x) 

print("--------------------")

x = x[0] #the first set of the list is the solution that we want

print("x[0]:", x[0])
print("x[1]:", x[1])
print("x[2]:", x[2])

print("--------------------")

print("x_1:", x[0])
print("x_2:", x[1])
print("x_3:", x[2])

"""
x:
{(2, -1, 1)}
--------------------
x:
[(2, -1, 1)]
--------------------
x[0]: 2
x[1]: -1
x[2]: 1
--------------------
x_1: 2
x_2: -1
x_3: 1
"""
