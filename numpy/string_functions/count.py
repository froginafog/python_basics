import numpy as np

s = "To Python or not to Python. That is the question."

print("s:")
print(s)
print("-------------------------------------------------")

sought_pattern = "th"

num_sought_pattern_found = np.char.count(s, sought_pattern)

print("The pattern \"" + sought_pattern + "\" was found " 
      + str(num_sought_pattern_found) + " times in the string.")

#A capital case letter is not the same as as its lower case equivalent.

"""
s:
To Python or not to Python. That is the question.
-------------------------------------------------
The pattern "th" was found 3 times in the string.
"""
