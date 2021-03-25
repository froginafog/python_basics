"""
Ax = kx
k is some constant number
The eignenvalues of this system is set of values k that satisfies this equation.
Solve
Ax = kx
Ax - kx = 0
AIx - kIx = 0
AIx - kIx = 0
(AI - kI)x = 0
(A - kI)x = 0
Solve
det(A - kI) = 0
The left-hand side of this equation gives a polinomial P(k) of some degree.
The degree of the polynomial is 2 if the matrix is a 2x2.
The degree of the polynomial is 3 if the matrix is a 3x3.
Solve
P(k) = 0.
The eignenvalues of this system is set of values k that satisfies this equation.
The eignenvectors of this system is the set if vectors x that satisfies this equation.
"""

from sympy import Matrix, pprint, Eq

A = [
        [ 0, 1, 1],
        [ 1, 0, 0],
        [ 1, 1, 1]
    ]

A = Matrix(A)

print("A:")
pprint(A)
print("---------------------------1-----------------------------")

eigenvalues = A.eigenvals() #returns the engenvalues of A in the form of a dictionary
                            #{eigenvalue_1: multiplicity_1, eigenvalue_2: multiplicity_2, eigenvalue_3: multiplicity_3}
print("the eigenvalues and their multiplicities are:")
print("eigenvalues:") 
pprint(eigenvalues)

print("---------------------------2-----------------------------")

eigenvectors = A.eigenvects() #returns the eigenvectors of A in the form of a list of tuples
print("the eigenvalues, multiplicities, and eigenvectors are:")
print("eigenvectors:")
pprint(eigenvectors)

print("---------------------------3-----------------------------")

k = list(eigenvalues) #convert the dictionary into a list
print("k:")
pprint(k)

print("---------------------------4-----------------------------")

#eigenvalues 
k_1 = k[0] 
k_2 = k[1] 
k_3 = k[2]
print("k_1:", k_1)
print("k_2:", k_2)
print("k_3:", k_3)

print("---------------------------5-----------------------------")

#get the list of tuples as individual list of lists
x_1 = eigenvectors[0][2]
x_2 = eigenvectors[1][2]
x_3 = eigenvectors[2][2]
print("x_1:")
pprint(x_1)
print()
print("x_2:")
pprint(x_2)
print()
print("x_3:")
pprint(x_3)

print("---------------------------6-----------------------------")

#convert the list of lists into individual lists

#eigenvectors
x_1 = x_1[0] 
x_2 = x_2[0] 
x_3 = x_3[0] 
print("x_1:")
pprint(x_1)
print()
print("x_2:")
pprint(x_2)
print()
print("x_3:")
pprint(x_3)



"""
A:
⎡0  1  1⎤
⎢       ⎥
⎢1  0  0⎥
⎢       ⎥
⎣1  1  1⎦
---------------------------1-----------------------------
the eigenvalues and their multiplicities are:
eigenvalues:
{-1: 1, 0: 1, 2: 1}
---------------------------2-----------------------------
the eigenvalues, multiplicities, and eigenvectors are:
eigenvectors:
⎡⎛       ⎡⎡-1⎤⎤⎞  ⎛      ⎡⎡0 ⎤⎤⎞  ⎛      ⎡⎡2/3⎤⎤⎞⎤
⎢⎜       ⎢⎢  ⎥⎥⎟  ⎜      ⎢⎢  ⎥⎥⎟  ⎜      ⎢⎢   ⎥⎥⎟⎥
⎢⎜-1, 1, ⎢⎢1 ⎥⎥⎟, ⎜0, 1, ⎢⎢-1⎥⎥⎟, ⎜2, 1, ⎢⎢1/3⎥⎥⎟⎥
⎢⎜       ⎢⎢  ⎥⎥⎟  ⎜      ⎢⎢  ⎥⎥⎟  ⎜      ⎢⎢   ⎥⎥⎟⎥
⎣⎝       ⎣⎣0 ⎦⎦⎠  ⎝      ⎣⎣1 ⎦⎦⎠  ⎝      ⎣⎣ 1 ⎦⎦⎠⎦
---------------------------3-----------------------------
k:
[2, -1, 0]
---------------------------4-----------------------------
k_1: 2
k_2: -1
k_3: 0
---------------------------5-----------------------------
x_1:
⎡⎡-1⎤⎤
⎢⎢  ⎥⎥
⎢⎢1 ⎥⎥
⎢⎢  ⎥⎥
⎣⎣0 ⎦⎦

x_2:
⎡⎡0 ⎤⎤
⎢⎢  ⎥⎥
⎢⎢-1⎥⎥
⎢⎢  ⎥⎥
⎣⎣1 ⎦⎦

x_3:
⎡⎡2/3⎤⎤
⎢⎢   ⎥⎥
⎢⎢1/3⎥⎥
⎢⎢   ⎥⎥
⎣⎣ 1 ⎦⎦
---------------------------6-----------------------------
x_1:
⎡-1⎤
⎢  ⎥
⎢1 ⎥
⎢  ⎥
⎣0 ⎦

x_2:
⎡0 ⎤
⎢  ⎥
⎢-1⎥
⎢  ⎥
⎣1 ⎦

x_3:
⎡2/3⎤
⎢   ⎥
⎢1/3⎥
⎢   ⎥
⎣ 1 ⎦
"""

