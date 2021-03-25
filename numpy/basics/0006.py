import numpy as np

a = [[0, 10, 20], [30, 40, 50], [60, 70, 80]]
a = np.array(a)
start = 0
end = 3
step = 1
print("a[0,start:end:step]:", a[0,start:end:step])
print("a[1,start:end:step]:", a[1,start:end:step])
print("a[2,start:end:step]:", a[2,start:end:step])
#start is inclusive
#end is exclusive

"""
a[0,start:end:step]: [ 0 10 20]
a[1,start:end:step]: [30 40 50]
a[2,start:end:step]: [60 70 80]
"""
