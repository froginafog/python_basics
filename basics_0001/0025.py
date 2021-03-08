ROWS = 3
COLUMNS = 4

#Create a ROWS X COLUMNS matrix with 0s.
A = [[0 for j in range(COLUMNS)] for i in range(ROWS)]

count = 0

for i in range(0, len(A)):
    for j in range(0, len(A[i])):
        A[i][j] = count
        count = count + 1

print("A:", A)

"""
A: [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
"""
