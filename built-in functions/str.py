#The str() function converts the specified value into a string.
a = [1.1, 2.2, 3.3, 4.4, 5.5]

b = [""] * len(a)

for i in range(0, len(a)):
    b[i] = str(a[i])

print("b:", b)

"""
b: ['1.1', '2.2', '3.3', '4.4', '5.5']
"""
