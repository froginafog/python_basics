#variance = standard_deviation^2

import statistics

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mean = statistics.mean(a)
variance = statistics.variance(a)

print("a:", a)
print("mean of a:", mean)
print("variance of a:", variance)

print("----------------------------------")

b = [3, 3, 4, 4, 5, 5, 6, 6, 7, 8]

mean = statistics.mean(b)
variance = statistics.variance(b)

print("b:", b)
print("mean of b:", mean)
print("variance of b:", variance)

"""
a: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean of a: 5.5
variance of a: 9.166666666666666
----------------------------------
b: [3, 3, 4, 4, 5, 5, 6, 6, 7, 8]
mean of b: 5.1
variance of b: 2.7666666666666666
"""
