import numpy as np

s = "To    Python     or    not    to    Python    ."

sought_pattern = "  "
replacement_pattern = " "
for i in range(0, 10):  #enough iterations to make all replacements
    s = np.char.replace(s, sought_pattern, replacement_pattern)
sought_pattern = " ."
replacement_pattern = "."
s = np.char.replace(s, sought_pattern, replacement_pattern)
    
print("|", end = "")
print(s, end = "")
print("|")

print("----------------------------------------")

sought_pattern = "Python"
replacement_pattern = "Javascript"
s = np.char.replace(s, sought_pattern, replacement_pattern)

print("|", end = "")
print(s, end = "")
print("|")

"""
|To Python or not to Python.|
----------------------------------------
|To Javascript or not to Javascript.|
"""
