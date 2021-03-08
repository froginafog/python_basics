a = [1, 2, 3, 4, 5]

print("a: ", end = "")
print(a)

num_elements = len(a)
for i in range(0, num_elements):
    a[i] = a[i] * 2

print("after modification:")
print("a: ", end = "")
print(a)

"""
a: [1, 2, 3, 4, 5]
after modification:
a: [2, 4, 6, 8, 10]
""" 
