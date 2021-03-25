"""
The Normal Distribution is one of the most important distributions.
It is also called the Gaussian Distribution.
It fits the probability distribution of many events.
Use the random.normal() method to get a Normal Data Distribution.

three parameters:
loc - (Mean) where the peak of the bell exists.
scale - (Standard Deviation) how flat the graph distribution should be.
size - The shape of the returned array.

"size" can be set to size = (rows, columns) for 2D array

The values will concentrate around the "mean" value.
The curve of a Normal Distribution is also known as the Bell Curve
because of the bell-shaped curve.
The x-axis will be the values around the mean.
The y-axis will be the frequencies of each value of the x-axis.
"""

import matplotlib.pyplot as plt
from numpy import random

#For a standard deviation of 2:

N = 1000 #number of elements with random values
mean = 5
standard_deviation = 1
y_data = random.normal(loc = mean, scale = standard_deviation, size = N)
plt.figure(0)
plt.hist(y_data)
plt.title("standard deviation = 1")
plt.xlabel("outcome of events")
plt.ylabel("frequencies")
plt.show(block = False) #prevent the plt.show() from blocking the flow of the program

#--------------------------------------------------
#For a standard deviation of 2:

N = 1000
mean = 5
standard_deviation = 2
y_data = random.normal(loc = mean, scale = standard_deviation, size = N)
plt.figure(1)
plt.hist(y_data)
plt.title("standard deviation = 2")
plt.xlabel("outcome of events")
plt.ylabel("frequencies")
plt.show(block = False)

#--------------------------------------------------
#For a standard deviation of 3:

N = 1000
mean = 5
standard_deviation = 3
y_data = random.normal(loc = mean, scale = standard_deviation, size = N)
plt.figure(2)
plt.hist(y_data)
plt.title("standard deviation = 3")
plt.xlabel("outcome of events")
plt.ylabel("frequencies")
plt.show(block = True)


