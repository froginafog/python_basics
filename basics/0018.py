inventory = ["apple", "tomato", "orange", "letus", "banana", "eggplant"]

fruits = [""] * 3
#we know that there are 3 kinds of fruits

vegetables = [""] * 3
#we know that there are 3 kinds of vegetables

fruits[0] = inventory[0]
fruits[1] = inventory[2]
fruits[2] = inventory[4]

vegetables[0] = inventory[1]
vegetables[1] = inventory[3]
vegetables[2] = inventory[5]

print("fruits:", fruits)
print("vegetables:", vegetables)

"""
fruits: ['apple', 'orange', 'banana']
vegetables: ['tomato', 'letus', 'eggplant']
"""
