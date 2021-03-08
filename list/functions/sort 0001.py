#sort() sorts the list ascending (by default)
inventory = ["cerry", "apple", "banana"]
numbers = [3, 2, 1, 5, 4]

print("sort ascending")
inventory.sort()
numbers.sort()
print("inventory:", inventory)
print("numbers:", numbers)

print("-------------------------------------------")

print("sort descending")
inventory.sort(reverse = True)
numbers.sort(reverse = True)
print("inventory:", inventory)
print("numbers:", numbers)

"""
sort ascending
inventory: ['apple', 'banana', 'cerry']
numbers: [1, 2, 3, 4, 5]
-------------------------------------------
sort descending
inventory: ['cerry', 'banana', 'apple']
numbers: [5, 4, 3, 2, 1]
"""
