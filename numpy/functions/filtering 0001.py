import numpy as np
a = [1, 2, 3, 4, 5]
a = np.array(a)

filter_array = [True, False, True, False, True]

a = a[filter_array]

print("a:", a)

"""
a: [1 3 5]
"""
