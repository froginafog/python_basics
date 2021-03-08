#The zip() function returns a zip object, which is an iterator of tuples
#where the first item in each passed iterator is paired together,
#and then the second item in each passed iterator are paired together etc.

fruits = ["apple", "orange", "banana"]
quantity = [10, 20, 30]

inventory = zip(fruits, quantity)
#"inventory" is now a matrix
print("inventory")
print(inventory)
print("-----------------------------------")

inventory = list(inventory)
print("inventory:", inventory)
print("len(inventory):", len(inventory)) #number of rows
print("len(inventory[0]):", len(inventory[0])) #number of columns in row 0
print("len(inventory[1]):", len(inventory[1])) #number of columns in row 1
print("len(inventory[2]):", len(inventory[2])) #number of columns in row 2
print("-----------------------------------")
for i in range(0, len(inventory)):
    for j in range(0, len(inventory[i])):
        print(inventory[i][j], end = " ")
    print()

"""
inventory: [('apple', 10), ('orange', 20), ('banana', 30)]
len(inventory): 3
len(inventory[0]): 2
len(inventory[1]): 2
len(inventory[2]): 2
-----------------------------------
apple 10 
orange 20 
banana 30 
"""
