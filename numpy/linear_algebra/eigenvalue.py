import numpy as np

A = [
        [ -2, -4,  2],
        [ -2,  1,  2],
        [  4,  2,  5]
    ]

A = np.array(A)

print("A:")
print(A)
print("------------------------")

"""
Ax = kx
k is some constant number
The eignenvalues of this system is set of values k that satisfies this equation.
Solve
Ax = kx
Ax - kx = 0
Ax - kIx = 0
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

eigenvalues, eigenvectors = np.linalg.eig(A)
print("the eigenvalues are:")
print("eigenvalues:") 
print(eigenvalues)
print("---------------------------------------------------------")
print("the eigenvectors are:")
print("eigenvectors:")
print(eigenvectors)
print("---------------------------------------------------------")
print("verify the solution")
print("check if Ax = kx is true for all k and x pairs")
#x is the set of eigenvectors
#k is the set of eigenvalues

k0 = eigenvalues[0]
k1 = eigenvalues[1]
k2 = eigenvalues[2]

#the columns of 'eigenvectors' are the eigenvectors
x0 = eigenvectors[:,0] 
x1 = eigenvectors[:,1]
x2 = eigenvectors[:,2]

print("A*x0:")
print(np.dot(A, x0)) #dot product between A with the first eigenvector of the system
#the first eigenvector of the system is the first column of x

print()

print("k0*x0:")
print(k0*x0) #product between the first eigenvalue of k with the first eigenvector of the system

print("---------------------------------------------------------")

print("A*x1:")
print(np.dot(A, x1)) #dot product between A with the second eigenvector of the system
#the second eigenvector of the system is the second column of x
print()

print("k1*x1:")
print(k1*x1) #product between the second eigenvalue of k with the second eigenvector of the system

print("---------------------------------------------------------")

print("A*x2:")
print(np.dot(A, x2)) #dot product between A with the third eigenvector of the system
#the third eigenvector of the system is the third column of x
print()

print("k2*x2:")
print(k2*x2) #product between the third eigenvalue of k with the third eigenvector of the system

"""
A:
[[-2 -4  2]
 [-2  1  2]
 [ 4  2  5]]
------------------------
the eigenvalues are:
eigenvalues:
[-5.  3.  6.]
---------------------------------------------------------
the eigenvectors are:
eigenvectors:
[[ 0.81649658  0.53452248  0.05842062]
 [ 0.40824829 -0.80178373  0.35052374]
 [-0.40824829 -0.26726124  0.93472998]]
---------------------------------------------------------
verify the solution
check if Ax = kx is true for all k and x pairs
A*x0:
[-4.0824829  -2.04124145  2.04124145]

k0*x0:
[-4.0824829  -2.04124145  2.04124145]
---------------------------------------------------------
A*x1:
[ 1.60356745 -2.40535118 -0.80178373]

k1*x1:
[ 1.60356745 -2.40535118 -0.80178373]
---------------------------------------------------------
A*x2:
[0.35052374 2.10314246 5.60837988]

k2*x2:
[0.35052374 2.10314246 5.60837988]
"""

