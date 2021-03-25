from numpy import random
import matplotlib.pyplot as plt

x = []

minimum = 0 #inclusive
maximum = 11 #exclusive

# random.randint(minimum,maximum) returns a number
# in the range from minimum (inclusive) to maximum (exclusive)

for i in range(0, 100):
    x.append(random.randint(minimum,maximum))

print("x:", x)

plt.hist(x)
plt.show()

"""
x: [3, 3, 5, 5, 4, 5, 3, 5, 3, 3]
"""
