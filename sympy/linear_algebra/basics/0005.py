from sympy import Matrix

A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

A = Matrix(A)

row_1_index_0_to_end = A.row(1)[0:]  #row 1 from index 0 to end

print("row_1_index_0_to_end:", row_1_index_0_to_end)

row_1_index_1_to_end = A.row(1)[1:] #row 1 from index 1 to end

print("row_1_index_1_to_end:", row_1_index_1_to_end)

"""
row_1_index_0_to_1: [4, 5, 6]
row_1_index_1_to_2: [5, 6]
"""
