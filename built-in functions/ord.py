#ord() returns the number representing the unicode code of a specified character

print("ord('a'):", ord('a'))
print("ord('b'):", ord('b'))
print("ord('c'):", ord('c'))
print("ord('x'):", ord('x'))
print("ord('y'):", ord('y'))
print("ord('z'):", ord('z'))
print("-----------------------")

value = ord('a')
for i in range(ord('a'), ord('z') + 1):
    print(chr(value) + " has the unicode value " + str(value))
    value = value + 1

"""
ord('a'): 97
ord('b'): 98
ord('c'): 99
ord('x'): 120
ord('y'): 121
ord('z'): 122
-----------------------
a has the unicode value 97
b has the unicode value 98
c has the unicode value 99
d has the unicode value 100
e has the unicode value 101
f has the unicode value 102
g has the unicode value 103
h has the unicode value 104
i has the unicode value 105
j has the unicode value 106
k has the unicode value 107
l has the unicode value 108
m has the unicode value 109
n has the unicode value 110
o has the unicode value 111
p has the unicode value 112
q has the unicode value 113
r has the unicode value 114
s has the unicode value 115
t has the unicode value 116
u has the unicode value 117
v has the unicode value 118
w has the unicode value 119
x has the unicode value 120
y has the unicode value 121
z has the unicode value 122
"""
