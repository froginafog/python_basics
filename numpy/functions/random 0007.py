from numpy import random

list_of_choices = [0, 1, 2]
list_of_probabilities = [0.2, 0.5, 0.3]
#the chance of getting a 0 is set to 0.2
#the chance of getting a 1 is set to 0.5
#the chance of getting a 2 is set to 0.3

number_of_elements = 10

x = random.choice(list_of_choices, p = list_of_probabilities, size = number_of_elements)

print("x:", x)

"""
x: [1 1 1 1 0 2 1 1 2 2]
"""
