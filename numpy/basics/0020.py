import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = np.array(a)
print("a:", a)

a_greater_than_5 = a > 5
a_equal_to_5 = a == 5
a_less_than_5 = a < 5

print("a_greater_than_5:", a_greater_than_5)
print("a_equal_to_5    :", a_equal_to_5)
print("a_less_than_5   :", a_less_than_5)

"""
a: [1 2 3 4 5 6 7 8 9]
a_greater_than_5: [False False False False False  True  True  True  True]
a_equal_to_5    : [False False False False  True False False False False]
a_less_than_5   : [ True  True  True  True False False False False False]
"""
