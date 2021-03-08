A = []

a1 = [11, 12, 13]
a2 = [21, 22, 23]
a3 = [31, 32, 33]

A = [a1, a2, a3]

num_rows = len(A)
for i in range(0, num_rows):
    num_columns = len(A[i])
    for j in range(0, num_columns):
        print(A[i][j], end = ' ')
    print()
    
"""
11 12 13 
21 22 23 
31 32 33
"""
