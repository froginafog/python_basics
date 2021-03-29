import re  

s = "abc $ 123 $ DEF # 456 @ ghi"

result = re.findall("[a-zA-Z]", s)
#returns a list of characters of the original string
#with only letters from 'a' to 'z' and 'A' to 'Z"

print("result:", result)

print("convert the list into a string")

result = ''.join(result)

print("result:", result)

"""
result: ['a', 'b', 'c', 'D', 'E', 'F', 'g', 'h', 'i']
convert the list into a string
result: abcDEFghi
"""
