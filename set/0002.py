#a set is a collection which is: unordered, unindexed, unchangeable, unique values
#a set is unordered because we cannot be sure in which order the elements will appear
#this is why we don't use indices when using sets
#unchangeable means we cannot change the values of the elements but we can add elements to the set
a = {4, 2, 1, 5, 3}

#the set is automatically put in ascending order

print("a:", a)

#print("a[0]:", a[0])  ERROR: 'set' object is not subscriptable

print("a:", end = " ")
for x in a:
    print(x, end = " ")

"""
a: {1, 2, 3, 4, 5}
a: 1 2 3 4 5 
"""
