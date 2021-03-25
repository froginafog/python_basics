import numpy as np

s = "python"

pattern = '-'
num_times = 6 #number of times that we want the pattern to be repeated
field_length = len(s) + num_times
s = np.char.center(s, field_length, pattern)
#padding both sides of a string with a chosen pattern

print("s:")
print(s)

"""
s:
---python---
"""
