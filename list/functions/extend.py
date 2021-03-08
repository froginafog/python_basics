#extend() adds the specified list elements
#(or any iterable) to the end of the current list.

inventory = ["apple", "orange", "peach"]
vegetables = ["carrot", "letus", "eggplant"]
inventory.extend(vegetables)

print("inventory:", inventory)

"""
inventory: ['apple', 'orange', 'peach', 'carrot', 'letus', 'eggplant']
"""
