A = [[11, 12, 13],
     [21, 22, 23],
     [31, 32, 33],
     [41, 42, 43]]

print("number of rows in A:", len(A))
print("number of columns in A[0]:", len(A[0]))
print("number of columns in A[1]:", len(A[1]))
print("number of columns in A[2]:", len(A[2]))
print("number of columns in A[3]:", len(A[3]))
print("-------------------------------------")
print("A:", A)
print("A[0]:", A[0])
print("A[1]:", A[1])
print("A[2]:", A[2])
print("A[3]:", A[3])
print("-------------------------------------")
print("A:")
for i in range(0, len(A)):
    for j in range(0, len(A[i])):
        print(A[i][j], end = " ")
    print()

"""
number of rows in A: 4
number of columns in A[0]: 3
number of columns in A[1]: 3
number of columns in A[2]: 3
number of columns in A[3]: 3
-------------------------------------
A: [[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]]
A[0]: [11, 12, 13]
A[1]: [21, 22, 23]
A[2]: [31, 32, 33]
A[3]: [41, 42, 43]
-------------------------------------
A:
11 12 13 
21 22 23 
31 32 33 
41 42 43
"""
