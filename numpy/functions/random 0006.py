from numpy import random

rows = 3
columns = 5
list_of_choice = [3, 6, 9]

#create a matrix of random numbers within the list of choice
M = random.choice(list_of_choice, size = (rows, columns))

print("M:")
print(M)

print("------------------------")

list_of_choice = [0, 1]
M = random.choice(list_of_choice, size = (rows, columns))

print("M:")
print(M)

"""
M:
[[6 9 3 9 6]
 [6 9 9 3 3]
 [3 9 9 6 6]]
------------------------
M:
[[0 0 1 0 0]
 [1 1 0 0 1]
 [0 0 1 0 0]]
"""
