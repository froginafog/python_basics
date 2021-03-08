N = 5 #number of elements
a = [0] * N #initialize an array of N elements with the value 0

for i in range(0, len(a)):
    print(a[i], end = " ")

print()
print("--------------------")

for i in range(0, len(a)):
    a[i] = i

for i in range(0, len(a)):
    print(a[i], end = " ")

"""
0 0 0 0 0 
--------------------
0 1 2 3 4
"""
