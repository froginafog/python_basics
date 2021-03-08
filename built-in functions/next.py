# The next() function returns the next item in an iterator.

# "default" (optional)
#If the iterator is exhausted (there is no next item),
#then next(it, default) returns the value stored in "default".

a = ["apple", "banana", "orange"]
it = iter(a)

sentinel = "----------------"

#"current" means current item
current = ""
while current != sentinel:
    current = next(it, sentinel)
    print("current:", current)

"""
current: apple
current: banana
current: orange
current: ----------------
"""
