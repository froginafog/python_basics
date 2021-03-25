import numpy as np

s = "ABC DEF GHI"

print("s:")
print(s)

print("----------------------------------")

separator = "."
s = np.char.join(separator, s)

print("s:")
print(s)

"""
s:
ABC DEF GHI
----------------------------------
s:
A.B.C. .D.E.F. .G.H.I
"""
