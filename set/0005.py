#a set is a collection which is: unordered, unindexed, unchangeable, unique values
#a set is unordered because we cannot be sure in which order the elements will appear
#unchangeable means we cannot change the values of the elements but we can add elements to the set
a = {1, 2, 3, 4, 5, 4, 3, 2, 1}

num_elements = len(a)

print("type(a):", type(a))
print("a:", a)
num_elements = len(a)
print("num_elements:", num_elements)

#print(a[0])  ERROR: 'set' object is not subscriptable

"""
type(a): <class 'set'>
a: {1, 2, 3, 4, 5}
num_elements: 5
"""
