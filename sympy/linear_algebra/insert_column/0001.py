from sympy import Matrix , pprint

A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

A = Matrix(A)

a = [1000, 2000, 3000]

a = Matrix(a)

A = A.col_insert(1, a) #insert 'a' into column 1 of A

num_rows = A.shape[0]
num_columns = A.shape[1]

print("num_rows:", num_rows)
print("num_columns:", num_columns)

print("A:")
pprint(A)

"""
num_rows: 3
num_columns: 4
A:
⎡1  1000  2  3⎤
⎢             ⎥
⎢4  2000  5  6⎥
⎢             ⎥
⎣7  3000  8  9⎦
"""
