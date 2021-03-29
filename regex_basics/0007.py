import re  

s = "abc $ 123 $ DEF $ 456 $ ghi"

result = re.findall("[^$]", s)
#returns a list of characters of the original string without '$ '

print("result:", result)

print("convert the list into a string")

result = ''.join(result)

print("result:", result)


"""
result: ['a', 'b', 'c', ' ', ' ', '1', '2', '3', ' ', ' ', 'D', 'E', 'F', ' ', ' ', '4', '5', '6', ' ', ' ', 'g', 'h', 'i']
convert the list into a string
result: abc  123  DEF  456  ghi
"""
