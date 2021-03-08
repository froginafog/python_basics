"""
"r" - read (default mode)
open a file for reading, error if the file does not exist
"""

file = open("0002.txt", "r")
num_chars = 5 #number of characters that we want to read
buffer = file.read(num_chars)
print("buffer:")
print(buffer)

"""
buffer:
To Py
"""

