import re  

s = "abc $ 123 $ DEF $ 456 $ ghi"

result = re.findall("[$]", s)
#returns a list of characters of the original string with '$'

print("result:", result)

if(len(result) > 0):
    print("'$'", "is found in the string")
else:
    print("'$'", "is not found in the string")


"""
result: ['$', '$', '$', '$']
'$' is found in the string
"""
