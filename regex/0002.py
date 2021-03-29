import re   #re stands for regular expression

s = "To Python or not to Python. To C++ or not to C++."

result = re.findall("[^PC]", s)
#returns a list of characters of the original string without P or C.

print("result:", result)

print("convert the list into a string")

result = ''.join(result)

print("result:", result)

"""
result: ['T', 'o', ' ', 'y', 't', 'h', 'o', 'n', ' ', 'o', 'r', ' ', 'n', 'o', 't', ' ', 't', 'o', ' ', 'y', 't', 'h', 'o', 'n', '.', ' ', 'T', 'o', ' ', '+', '+', ' ', 'o', 'r', ' ', 'n', 'o', 't', ' ', 't', 'o', ' ', '+', '+', '.']
convert the list into a string
result: To ython or not to ython. To ++ or not to ++.
"""
