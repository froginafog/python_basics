from sympy import Matrix, pprint

A = [
        [1, 2, 3],
        [2, 3, 2],
        [3, 2, 1]
    ]

A = Matrix(A)
A_inverse = A.inv() #inverse of A

print("A_inverse:")
pprint(A_inverse)

"""
A_inverse:
⎡1/8   -1/2  5/8 ⎤
⎢                ⎥
⎢-1/2   1    -1/2⎥
⎢                ⎥
⎣5/8   -1/2  1/8 ⎦
"""
