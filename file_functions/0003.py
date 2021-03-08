"""
"r" - read (default mode)
open a file for reading, error if the file does not exist
"""

file = open("0003.txt", "r")

buffer = file.readline() #store one line of what is read to buffer
print("buffer:")
print(buffer)

buffer = file.readline() #store another line of what is read to buffer
print("buffer:")
print(buffer)

file.close() #close the file

"""
buffer:
To Py or not to Py.

buffer:
That is the question.
"""
