#The standard deviation measures of how spread out the numbers are
#relative to the mean.
#A higher standard deviation means the data is farther from the mean.
#A lower standard deviation means the data is closer to the mean.

import statistics

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mean = statistics.mean(a)
standard_deviation = statistics.stdev(a)

print("a:", a)
print("mean of a:", mean)
print("standard deviation of a:", standard_deviation)

print("----------------------------------")

b = [3, 3, 4, 4, 5, 5, 6, 6, 7, 8]

mean = statistics.mean(b)
standard_deviation = statistics.stdev(b)

print("b:", b)
print("mean of b:", mean)
print("standard deviation of b:", standard_deviation)

"""
a: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean of a: 5.5
standard deviation of a: 3.0276503540974917
----------------------------------
b: [3, 3, 4, 4, 5, 5, 6, 6, 7, 8]
mean of b: 5.1
standard deviation of b: 1.66332999331662
"""
