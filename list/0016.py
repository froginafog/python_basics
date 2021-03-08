#count()  returns the number of elements with the specified value

a = [1, 2, 2, 3, 3, 3, 4, 4, 5]

print("a:", a)
print("There are " + str(a.count(1)) + " elements with the value 1 in a[].")
print("There are " + str(a.count(2)) + " elements with the value 2 in a[].")
print("There are " + str(a.count(3)) + " elements with the value 3 in a[].")
print("There are " + str(a.count(4)) + " elements with the value 4 in a[].")
print("There are " + str(a.count(5)) + " elements with the value 5 in a[].")

"""
a: [1, 2, 2, 3, 3, 3, 4, 4, 5]
There are 1 elements with the value 1 in a[].
There are 2 elements with the value 2 in a[].
There are 3 elements with the value 3 in a[].
There are 2 elements with the value 4 in a[].
There are 1 elements with the value 5 in a[].
"""
