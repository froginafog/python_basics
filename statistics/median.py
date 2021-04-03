"""
The median is the value in the middle of the set.
"""

import statistics

a = [1, 2, 3, 4, 5, 7, 8, 9, 10]

median = statistics.median(a)

print("median of a:", median)

b = [1, 2, 3, 4, 5, 7, 8, 9]

median = statistics.median(b)
#since the middle value is not exactly one value, we do (4 + 5)/2

print("median of b:", median)

"""
median of a: 5
median of b: 4.5
"""
