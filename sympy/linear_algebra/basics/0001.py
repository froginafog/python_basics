from sympy.matrices import Matrix

A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

A = Matrix(A)

print("A:")
print(A)

num_rows = A.shape[0]
num_columns = A.shape[1]

print("num_rows:", num_rows)
print("num_columns:", num_columns)

print("A:")
for i in range(0, num_rows):
    for j in range(0, num_columns):
        print(A[i,j], end = ' ') #we cannot use A[i][j] for sympy matrix
    print()

"""
A:
Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
num_rows: 3
num_columns: 3
A:
1 2 3 
4 5 6 
7 8 9
"""
