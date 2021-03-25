import numpy as np

A = [[11, 12, 13, 14, 15, 16, 17, 18, 19],
     [21, 22, 23, 24, 25, 26, 27, 28, 29],
     [31, 32, 33, 34, 35, 36, 37, 38, 39],
     [41, 42, 43, 44, 45, 46, 47, 48, 49],
     [51, 52, 53, 54, 55, 56, 57, 58, 59]]

A = np.array(A)

print("A:")
print(A)

print("-------------------------------------------------")

#A[row_index , column_index] 
A_row_2_column_4 = A[2 , 4]
print("A_row_2_column_4:")
print(A_row_2_column_4)

print("-------------------------------------------------")

#A[row_index , column_start:column_end] 
A_row_2 = A[2 , :]
print("A_row_2:")
print(A_row_2)

print("-------------------------------------------------")

#A[row_start:row_end , column_index]  
A_column_4 = A[: , 4]
print("A_column_4:")
print(A_column_4)

print("-------------------------------------------------")

#A[row_start:row_end , column_start:column_end]

#row_start is inclusive
#row_end is exclusive

#column_start is inclusive
#column_end is exclusive

#putting nothing before and after ':' means full range

A_rows_1_to_3 = A[1:(3+1) , :] 
print("A_rows_1_to_3:")
print(A_rows_1_to_3)

print("-------------------------------------------------")

#A[row_start:row_end , column_start:column_end]

#row_start is inclusive
#row_end is exclusive

#column_start is inclusive
#column_end is exclusive

#putting nothing before and after ':' means full range

A_columns_3_to_5 = A[: , 3:(5+1)]
print("A_columns_3_to_5:")
print(A_columns_3_to_5)

print("-------------------------------------------------")

#A[row_start:row_end , column_start:column_end]

#row_start is inclusive
#row_end is exclusive

#column_start is inclusive
#column_end is exclusive

A_rows_1_to_3_columns_3_to_5 = A[1:(3+1) , 3:(5+1)]
print("A_rows_1_to_3_columns_3_to_5:")
print(A_rows_1_to_3_columns_3_to_5)


