from sympy import Matrix

A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

A = Matrix(A)

col_1_index_0_to_end = A.col(1)[0:]  #col 1 from index 0 to end

print("col_1_index_0_to_end:", col_1_index_0_to_end)

col_1_index_1_to_end = A.col(1)[1:] #col 1 from index 1 to end

print("col_1_index_1_to_end:", col_1_index_1_to_end)

"""
col_1_index_0_to_end: [2, 5, 8]
col_1_index_1_to_end: [5, 8]
"""
