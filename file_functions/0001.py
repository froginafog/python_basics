"""
"r" - read (default mode)
open a file for reading, error if the file does not exist
"""

file = open("0001.txt", "r")
buffer = file.read() #store what is read to buffer
print("buffer:")
print(buffer)

"""
buffer:
To Py or not to Py.
That is the question.
"""
