# append()  adds an element at the end of the list

a = []

print("a:", a)

for i in range(0, 10):
    a.append(i)

print("a:", a)

a.clear()

print("a.clear() is called")

print("a:", a)

"""
a: []
a: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.clear() is called
a: []
"""
