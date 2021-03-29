import re  

s = "abc $ 123 $ def # 456 @ ghi"

result = re.findall("[a-z]", s)
#returns a list of characters of the original string
#with only letters from 'a' to 'z'

print("result:", result)

print("convert the list into a string")

result = ''.join(result)

print("result:", result)

"""
result: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
convert the list into a string
result: abcdefghi
"""
