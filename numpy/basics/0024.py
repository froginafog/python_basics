import numpy as np

minimum = 1  #inclusive
maximum = 10 #exclusive

step = 1
a_step_1 = np.arange(minimum, maximum, step)
#create an array within a range of values
print("a_step_1:", a_step_1)

step = 2
a_step_2 = np.arange(minimum, maximum, step)
print("a_step_2:", a_step_2)

"""
a_step_1: [1 2 3 4 5 6 7 8 9]
a_step_2: [1 3 5 7 9]
"""
