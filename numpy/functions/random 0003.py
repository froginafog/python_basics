from numpy import random
import matplotlib.pyplot as plt

minimum = 0  #inclusive
maximum = 11 #exclusive
number_of_numbers = 10 #sample size
x = random.randint(minimum, maximum, size = number_of_numbers)

print("x:", x)

plt.hist(x)
plt.show()

"""
x: [5 6 6 7 9 5 7 6 6 8]
"""
