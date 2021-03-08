#Convert a sring to a list.
#Modify the list.
#Convert the list back to a string.

s = "abc def ghi" 
print("s:", s)

#We cannot change the characters of a string individually.
#Therefore, we convert the string into a list.

print("convert the string to a list")

s = list(s)
print("s:", s)

print("modify the list")
s[4] = 'x'
s[5] = 'y'
s[6] = 'z'

print("s:", s)

print("convert the list back to a string")

separator = ''
s = separator.join(s)
print("s:", s)


"""
s: abc def ghi
convert the string to a list
s: ['a', 'b', 'c', ' ', 'd', 'e', 'f', ' ', 'g', 'h', 'i']
modify the list
s: ['a', 'b', 'c', ' ', 'x', 'y', 'z', ' ', 'g', 'h', 'i']
convert the list back to a string
s: abc xyz ghi
"""
