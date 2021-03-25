import numpy as np

a = ['To', 'Python', 'or', 'not', 'to', 'Python.']
a = np.array(a)

s = ""
num_strings = len(a)
for i in range(0, num_strings):
    s = np.char.add(s, a[i])
    s = np.char.add(s, " ")

#we use np.char.add() because we cannot concatenate
#numpy strings

print("a:")
print(a)

print("---------------------------------------------------")

print("s:")
print(s)

"""
a:
['To' 'Python' 'or' 'not' 'to' 'Python.']
---------------------------------------------------
s:
To Python or not to Python. 
"""
