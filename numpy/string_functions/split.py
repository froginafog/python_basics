import numpy as np

s = "To Python or not to Python."

separator = " "
a = np.char.split(s, separator)
#splitting the string into an array of substrings

print("s:")
print(s)
print("a:")
print(a)

"""
s:
To Python or not to Python.
a:
['To', 'Python', 'or', 'not', 'to', 'Python.']
"""
