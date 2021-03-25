"""
Binomial Distribution is a Discrete Distribution.
It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
It has three parameters:
n - number of trials.
p - probability of occurence of each trial (e.g. toss a coin: p = 0.5 for each trial).
size - The shape of the returned array.
"""

from numpy import random

N = 20 #number of elements
number_trials = 10000
probability = 0.5
M = random.binomial(n = number_trials, p = probability, size = N)
print("M:")
print(M)

"""
M:
[5058 5023 5131 5073 4931 5034 5000 4975 4975 4962 5123 5057 5058 4983
 4928 5040 5034 5045 5017 4944]
"""
