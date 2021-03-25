import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = np.array(a)

even_pass_filter = [] #filter for keeping even numbers

for n in a:
    if n % 2 == 0: #n is even
        even_pass_filter.append(True)
    else: #n is odd
        even_pass_filter.append(False)

a_even = a[even_pass_filter]

print("a:", a)
print("a_even:", a_even)

"""
a: [1 2 3 4 5 6 7 8 9]
a_even: [2 4 6 8]
"""
