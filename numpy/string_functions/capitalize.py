import numpy as np

s = "to python or not to python. that is the question."

s = np.char.capitalize(s)
#Only the first character of the string is capitalized.

print("s:")
print(s)

"""
s:
To python or not to python. that is the question.
"""
