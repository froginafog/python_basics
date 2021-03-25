import numpy as np

A = [[11, 12, 13, 14, 15],
     [21, 22, 23, 24, 25],
     [31, 32, 33, 34, 35]]

A = np.array(A)

print("A:")
print(A)

print("-------------------------------------")

print("shape of A:", A.shape)
print("number of rows in A:", A.shape[0])
print("number of columns in A:", A.shape[1])

print("-------------------------------------")

print("A:")
num_rows = A.shape[0]  
for i in range(0, num_rows):
    num_columns = A[i].shape[0]
    for j in range(0, num_columns):
        print(A[i,j], end = ' ')
    print()

print("-------------------------------------")

row_0 = A[0,:]
row_1 = A[1,:]
row_2 = A[2,:]

print("row_0:", row_0)
print("row_1:", row_1)
print("row_2:", row_2)

print("-------------------------------------")

column_0 = A[:,0]
column_1 = A[:,1]
column_2 = A[:,2]
column_3 = A[:,3]
column_4 = A[:,4]

print("column_0:", column_0)
print("column_1:", column_1)
print("column_2:", column_2)
print("column_3:", column_3)
print("column_4:", column_4)

print("-------------------------------------")

#A[row_starting_index:row_ending_index, column_starting_index:column_ending_index]
#row_starting_index is inclusive
#row_ending_index is exlusive
#column_starting_index is inclusive
#column_ending_index is exclusive
print("A[0:2,0:2]:")
print(A[0:2,0:2])

print("-------------------------------------")

print("A[1:3,0:2]:")
print(A[1:3,0:2])

"""
A:
[[11 12 13 14 15]
 [21 22 23 24 25]
 [31 32 33 34 35]]
-------------------------------------
shape of A: (3, 5)
number of rows in A: 3
number of columns in A: 5
-------------------------------------
A:
11 12 13 14 15 
21 22 23 24 25 
31 32 33 34 35 
-------------------------------------
row_0: [11 12 13 14 15]
row_1: [21 22 23 24 25]
row_2: [31 32 33 34 35]
-------------------------------------
column_0: [11 21 31]
column_1: [12 22 32]
column_2: [13 23 33]
column_3: [14 24 34]
column_4: [15 25 35]
-------------------------------------
A[0:2,0:2]:
[[11 12]
 [21 22]]
-------------------------------------
A[1:3,0:2]:
[[21 22]
 [31 32]]
"""

