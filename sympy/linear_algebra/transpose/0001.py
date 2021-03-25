from sympy import Matrix, pprint

A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

A = Matrix(A)
A_T = A.T #transpose of A

print("A_T:")
pprint(A_T)

"""
A_T:
⎡1  4  7⎤
⎢       ⎥
⎢2  5  8⎥
⎢       ⎥
⎣3  6  9⎦
"""
