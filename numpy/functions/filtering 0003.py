import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = np.array(a)

even_pass_filter = a % 2 == 0
#filter for keeping even numbers

a_even = a[even_pass_filter]

print("even_pass_filter:", even_pass_filter)
print("a_even:", a_even)

"""
even_pass_filter: [False  True False  True False  True False  True False]
a_even: [2 4 6 8]
"""
