import re  

s = "abc\t123\nDEF\t456\nghi\t789"

print("s:")
print(s)

print("----------------------------------------------------------")

result = re.findall("[^\t\n]", s)
#returns a list of characters of the original string without \t (tab) \n (newline)

print("result:", result)

print("convert the list into a string")

result = ''.join(result)

print("result:", result)


"""
s:
abc	123
DEF	456
ghi	789
----------------------------------------------------------
result: ['a', 'b', 'c', '1', '2', '3', 'D', 'E', 'F', '4', '5', '6', 'g', 'h', 'i', '7', '8', '9']
convert the list into a string
result: abc123DEF456ghi789
"""
