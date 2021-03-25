import numpy as np

s = "    To C or not to C.     "
s = np.char.strip(s)
print("|", end = "")
print(s, end = "")
print("|")

"""
|To C or not to C.|
"""
