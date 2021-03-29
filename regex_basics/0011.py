import re  

s = "To # Python ! or % not @ to ^ Python. That is, well, the question."

print("s:")
print(s)

print("----------------------------------------------------------")

result = re.findall("[a-zA-Z1-9,.]", s)
#returns a list with only alphabets, numbers, commas, and periods

print("result:")
print(result)

print("----------------------------------------------------------")

print("convert the list into a string")

result = ''.join(result)

print("result:")
print(result)

"""
s:
To # Python ! or % not @ to ^ Python. That is, well, the question.
----------------------------------------------------------
result:
['T', 'o', 'P', 'y', 't', 'h', 'o', 'n', 'o', 'r', 'n', 'o', 't', 't', 'o', 'P', 'y', 't', 'h', 'o', 'n', '.', 'T', 'h', 'a', 't', 'i', 's', ',', 'w', 'e', 'l', 'l', ',', 't', 'h', 'e', 'q', 'u', 'e', 's', 't', 'i', 'o', 'n', '.']
----------------------------------------------------------
convert the list into a string
result:
ToPythonornottoPython.Thatis,well,thequestion.
"""
