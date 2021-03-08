"""
The enumerate() function takes a collection (e.g. a tuple)
and returns it as an enumerate object.
"""

x = ("apple", "orange", "banana")

start = 0
x_enumerate = enumerate(x, start)
print("list(x_enumerate):", list(x_enumerate))

start = 1
x_enumerate = enumerate(x, start)
print("list(x_enumerate):", list(x_enumerate))


"""
list(x_enumerate): [(0, 'apple'), (1, 'orange'), (2, 'banana')]
list(x_enumerate): [(1, 'apple'), (2, 'orange'), (3, 'banana')]
"""
