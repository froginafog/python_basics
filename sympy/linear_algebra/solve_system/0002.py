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

A_aug_b = [A,b] #augmented matrix (A is augmented with b)

print("A_aug_b:")
pprint(A_aug_b)

x = linsolve(A_aug_b)
#x = {[x_1, x_2, x_3]}
#The type of x is <class 'sympy.sets.sets.FiniteSet'>

x = list(x) #convert to list

x = x[0] #the first set of the list is the solution that we want

print()

print("x_1:", x[0])
print("x_2:", x[1])
print("x_3:", x[2])

"""
A_aug_b:
⎡⎡1   -2  3 ⎤  ⎡ 7 ⎤⎤
⎢⎢          ⎥  ⎢   ⎥⎥
⎢⎢2   1   1 ⎥, ⎢ 4 ⎥⎥
⎢⎢          ⎥  ⎢   ⎥⎥
⎣⎣-3  2   -2⎦  ⎣-10⎦⎦

x_1: 2
x_2: -1
x_3: 1
"""
