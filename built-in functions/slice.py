#The slice() function returns a slice object.
#A slice object is used to specify how to slice a sequence.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

segment1 = slice(3)
start = 3 #inclusive
end = 6 #exclusive
segment2 = slice(start, end)

print("a[segment1]:", a[segment1])
print("a[segment2]:", a[segment2])

"""
a[segment1]: [1, 2, 3]
a[segment2]: [4, 5, 6]
"""
