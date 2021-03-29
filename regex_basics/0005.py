import re  

s = "abc $ 123 $ DEF # 456 @ ghi"

result = re.findall("[0-9]", s)
#returns a list of characters of the original string
#with only digits from '0' to '9'

print("result:", result)

print("convert the list into a string")

result = ''.join(result)

print("result:", result)

"""
result: ['1', '2', '3', '4', '5', '6']
convert the list into a string
result: 123456
"""
