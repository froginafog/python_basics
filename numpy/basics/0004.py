import numpy as np

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
a = np.array(a)
print("a[3:]:", a[3:]) 
print("a[:3]:", a[:3]) 

#[start:end]
#start is inclusive
#end is exclusive

"""
a[3:]: [ 30  40  50  60  70  80  90 100]
a[:3]: [ 0 10 20]
"""

