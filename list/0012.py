a = [7, 8, 9, 1, 2, 0, 3, 5, 4, 6]

print("a:", a);
a.sort();
print("a.sort() is called")
print("a:", a);
a.sort(reverse = True)
print("a.sort(reverse = True) is called")
print("a:", a);

"""
a: [7, 8, 9, 1, 2, 0, 3, 5, 4, 6]
a.sort() is called
a: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.sort(reverse = True) is called
a: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""
