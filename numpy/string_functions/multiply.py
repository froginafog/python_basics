import numpy as np

pattern = '-'
num_times = 5 #the number of times that we wish to repeat the pattern
dashes = np.char.multiply(pattern, num_times)
print(dashes)


"""
-----
"""
