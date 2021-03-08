from copy import deepcopy

def print_matrix(A):
    num_rows = len(A)
    num_columns = len(A[0])
    max_length_of_each_column = [0] * num_columns
    #find the maximum lengths of each column so that we can format the output
    for i in range(0, num_rows):
        for j in range(0, num_columns):
            length = len(str(A[i][j]))
            if(length > max_length_of_each_column[j]):
                max_length_of_each_column[j] = length
    #format and print the elements of the matrix
    for i in range(0, num_rows):
        for j in range(0, num_columns):
            s = str(A[i][j])
            formatter = "%" + str(max_length_of_each_column[j] + 1) + "s"
            s = formatter % s
            print(s, end = '')
        print()

A = [[11, 12, 13],
     [21, 22, 23],
     [31, 32, 33]
    ]

A_shallow_copy = A
#Changes done to 'A' later will be reflected on 'A_shallow_copy'.
#This is a memory copy.

A_deep_copy = deepcopy(A)
#Changes done to 'A' later will NOT be reflected on 'A_deep_copy'.
#This is a value copy.

A[1][1] = 0

print("A_shallow_copy:")
print_matrix(A_shallow_copy)
print("-------------------------")
print("A_sdeep_copy:")
print_matrix(A_deep_copy)
    
"""
A_shallow_copy:
 11 12 13
 21  0 23
 31 32 33
-------------------------
A_deep_copy:
 11 12 13
 21 22 23
 31 32 33
"""
