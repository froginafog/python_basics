#a set is a collection which is: unordered, unindexed, unchangeable, unique values
#a set is unordered because we cannot be sure in which order the elements will appear
#this is why we don't use indices when using sets
#unchangeable means we cannot change the values of the elements but we can add elements to the set
a = {1, 2, 3, 4, 5}

if 3 in a:
    print(3, "is in the set")
else:
    print(3, "is not in the set")

if 10 in a:
    print(10, "is in the set")
else:
    print(10, "is not in the set")


"""
3 is in the set
10 is not in the set
"""
