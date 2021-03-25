import numpy as np

a = np.array([1, 2, 3, 4, 5])

a_copy = a.copy()
a_view = a.view()

print("a_copy.base:", a_copy.base)
print("a_view.base:", a_view.base)

"""
a_copy.base: None
a_view.base: [1 2 3 4 5]
"""
