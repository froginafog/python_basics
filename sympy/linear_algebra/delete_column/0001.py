
from sympy import Matrix, pprint

A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

A = Matrix(A)

A.col_del(1) #delete column 1 from matrix A

num_rows = A.shape[0]
num_columns = A.shape[1]

print("num_rows:", num_rows)
print("num_columns:", num_columns)

print("A:")
pprint(A)


"""
num_rows: 3
num_columns: 2
A:
⎡1  3⎤
⎢    ⎥
⎢4  6⎥
⎢    ⎥
⎣7  9⎦
"""
