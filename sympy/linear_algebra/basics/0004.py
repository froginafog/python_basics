from sympy import Matrix

A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

A = Matrix(A)

row_1_index_0_to_1 = A.row(1)[0:2]  #A.row(1)[inclusive:exclusive]

print("row_1_index_0_to_1:", row_1_index_0_to_1)

row_1_index_1_to_2 = A.row(1)[1:3] #A.row(2)[inclusive:exclusive]

print("row_1_index_1_to_2:", row_1_index_1_to_2)

"""
row_1_index_0_to_1: [4, 5]
row_1_index_1_to_2: [5, 6]
"""
