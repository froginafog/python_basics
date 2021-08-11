"""
The median is the value in the middle of the set.
"""

import statistics

a = [1, 2, 3, 4, 5, 7, 8, 9, 10]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
median_a = statistics.median(a)
print("median_a:", median_a)

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
median_b = statistics.median(b)
print("median_b:", median_b)

"""
median_a: 5.5
median_b: 5
"""
