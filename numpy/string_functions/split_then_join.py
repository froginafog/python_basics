import numpy as np

s = "ABC DEF GHI"

print("s:")
print(s)

print("-----------------------")

separator = " "
s = np.char.split(s, separator)
print("s:")
print(s)

print("-----------------------")

separator = "."
s = np.char.join(separator, s)
print("s:")
print(s)

"""
s:
ABC DEF GHI
-----------------------
s:
['ABC', 'DEF', 'GHI']
-----------------------
s:
ABC.DEF.GHI
"""
