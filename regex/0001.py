import re   #re stands for regular expression

s = "To Python or not to Python. To C++ or not to C++."

result = re.findall("[PC]", s)
#returns a list of characters of the original string where P and C are present.

print("result:", result)

print("convert the list into a string")

result = ''.join(result)

print("result:", result)

"""
result: ['P', 'P', 'C', 'C']
convert the list into a string
result: PPCC
"""
