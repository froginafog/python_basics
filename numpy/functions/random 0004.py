from numpy import random

rows = 3
columns = 5
minimum = 5  #inclusive
maximum = 10 #exclusive

#create a matrix of random integers
M = random.randint(minimum, maximum, size = (rows, columns))

print("M:")
print(M) 

"""
M:
[[5 9 5 6 6]
 [5 8 5 9 6]
 [6 9 7 6 9]]
"""
