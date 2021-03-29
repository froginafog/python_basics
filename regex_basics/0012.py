import re  

s = "To #     Python !    or % not @ to ^ Python.   That is,   well,    the    question."

print("s:")
print(s)

print("----------------------------------------------------------")

result = re.findall("[a-zA-Z0-9,.\s]", s) 
#returns a list with only alphabets, numbers, commas, and periods
#keep 'a' to 'z'
#keep 'A' to 'Z'
#keep '0' to '9'
#keep ','
#keep '.'
#keep '\s' (which is blank space)

print("result:")
print(result)

print("----------------------------------------------------------")

print("convert the list into a string")

result = ''.join(result)

print("result:")
print(result)

print("----------------------------------------------------------")

print("replace multi-spaces with a single space")

result = re.sub("\s+", " ", result)

print("result:")
print(result)

"""
s:
To #     Python !    or % not @ to ^ Python.   That is,   well,    the    question.
----------------------------------------------------------
result:
['T', 'o', ' ', ' ', ' ', ' ', ' ', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', ' ', ' ', ' ', ' ', 'o', 'r', ' ', ' ', 'n', 'o', 't', ' ', ' ', 't', 'o', ' ', ' ', 'P', 'y', 't', 'h', 'o', 'n', '.', ' ', ' ', ' ', 'T', 'h', 'a', 't', ' ', 'i', 's', ',', ' ', ' ', ' ', 'w', 'e', 'l', 'l', ',', ' ', ' ', ' ', ' ', 't', 'h', 'e', ' ', ' ', ' ', ' ', 'q', 'u', 'e', 's', 't', 'i', 'o', 'n', '.']
----------------------------------------------------------
convert the list into a string
result:
To      Python     or  not  to  Python.   That is,   well,    the    question.
----------------------------------------------------------
replace multi-spaces with a single space
result:
To Python or not to Python. That is, well, the question.
"""
