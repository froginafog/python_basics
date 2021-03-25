import numpy as np

rows = 2
columns = 5

a = np.zeros((rows, columns)) #create a 2D array of zeros 
print("a:")
print(a)
print("-----------------------------")

value = 1
b = np.full((rows, columns), value) #create a 2D array of ones
print("b:")
print(b)
print("-----------------------------")

c = np.random.random((rows, columns)) #create a 2D array of random numbers
                                      #in the range 0.0 to 1.0
print("c:")
print(c)
print("-----------------------------")

"""
a:
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
-----------------------------
b:
[[1 1 1 1 1]
 [1 1 1 1 1]]
-----------------------------
c:
[[0.9183878  0.26511026 0.11757577 0.71796408 0.60121119]
 [0.18332035 0.23303276 0.00983769 0.6876311  0.40236104]]
-----------------------------
"""
