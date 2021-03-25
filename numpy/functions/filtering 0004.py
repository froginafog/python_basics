import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = np.array(a)
print("a:", a)

greater_than_5_filter = a > 5

a_greater_than_5 = a[greater_than_5_filter]
print("a_greater_than_5:", a_greater_than_5)

less_than_5_filter = a < 5

a_less_than_5 = a[less_than_5_filter]
print("a_less_than_5:", a_less_than_5)

"""
a: [1 2 3 4 5 6 7 8 9]
a_greater_than_5: [6 7 8 9]
a_less_than_5: [1 2 3 4]
"""
