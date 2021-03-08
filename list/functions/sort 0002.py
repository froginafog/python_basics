inventory = ["apple", "strawberry", "orange"]
numbers = [[1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3], [1], [1, 2]]

def getLength(value):
    return len(value)

#Sort the list by the length of the values
inventory.sort(key = getLength)
print("inventory:", inventory)

numbers.sort(key = getLength)
print("numbers:", numbers)

"""
inventory: ['apple', 'orange', 'strawberry']
numbers: [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
"""
