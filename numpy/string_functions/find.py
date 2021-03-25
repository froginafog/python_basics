import numpy as np

original_string = "To Python or not to Python."
sought_string = "Python"

position = np.char.find(original_string, sought_string, start = 0, end = None)

if(position >= 0):
    print("The sought string is located at the position", position, "of the original string.")
else:
    print("The sought string cannot be found in the original string.")

print("-------------------------------------------------------------------------")

original_string = "To Python or not to Python."
sought_string = "C++"

position = np.char.find(original_string, sought_string, start = 0, end = None)

if(position >= 0):
    print("The sought string is located at the position", position, "of the original string.")
else:
    print("The sought string cannot be found in the original string.")

"""
The sought string is located at the position 3 of the original string.
-------------------------------------------------------------------------
The sought string cannot be found in the original string.
"""
