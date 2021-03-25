import numpy as np
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = np.array(a)

#split "a" into an array of 3 sub-arrays
a_split_into_3 = np.array_split(a, 3) 

print("a:", a)
print("a_split_into_3:", a_split_into_3)
print("a_split_into_3[0]:", a_split_into_3[0])
print("a_split_into_3[1]:", a_split_into_3[1])
print("a_split_into_3[2]:", a_split_into_3[2])

"""
a: [1 2 3 4 5 6 7 8 9]
a_split_into_3: [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]
a_split_into_3[0]: [1 2 3]
a_split_into_3[1]: [4 5 6]
a_split_into_3[2]: [7 8 9]
"""
