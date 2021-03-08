"""
"w" - write
open a file for writing, create the file if it does not exist
if a file already exists, that file gets overwritten
"""

file = open("0005.txt", "w")
buffer = "To Py or not to Py.\nThat is the question."
file.write(buffer)
file.close()

file = open("0005.txt", "a")
buffer = "\nI am you and you are me."
file.write(buffer)
file.close()

#we have to close the file before the content in "buffer"
#can appear in the file

file = open("0005.txt", "r")
buffer = file.read()
file.close()
print("buffer:")
print(buffer)

"""
buffer:
To Py or not to Py.
That is the question.
I am you and you are me.
"""
