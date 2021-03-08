#count() returns the number of elements with the specified value.
fruits = ["apple", "orange", "melon", "apple", "apple"]
numbers = [3, 2, 1, 3, 3]

print("fruits.count(\"apple\"):", fruits.count("apple"))
print("fruits.count(\"orange\"):", fruits.count("orange"))
print("fruits.count(\"strawberry\"):", fruits.count("strawberry"))
print("-------------------")
print("numbers.count(3):", numbers.count(3))

"""
fruits.count("apple"): 3
fruits.count("orange"): 1
fruits.count("strawberry"): 0
-------------------
numbers.count(3): 3
"""
