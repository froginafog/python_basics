"""
"w" - write
open a file for writing, create the file if it does not exist
if a file already exists, then the file gets overwritten
"""

file = open("0004.txt", "w")

buffer = "To Py or not to Py.\nThat is the question."

file.write(buffer)

file.close()
#we have to close the file before the content in "buffer"
#can appear in the file
