import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print("a:", a)
print("b:", b)

print("------------------")

hstack_a_on_b = np.hstack((a,b)) #horizontal stacking
print("hstack_a_on_b:")
print(hstack_a_on_b)

print("------------------")

vstack_a_on_b = np.vstack((a,b)) #vertical stacking
print("vstack_a_on_b:")
print(vstack_a_on_b)

print("------------------")

dstack_a_on_b = np.dstack((a,b)) #depth stacking (stacking columns)
print("dstack_a_on_b:")
print(dstack_a_on_b)

"""
a: [1 2 3]
b: [4 5 6]
------------------
hstack_a_on_b:
[1 2 3 4 5 6]
------------------
vstack_a_on_b:
[[1 2 3]
 [4 5 6]]
------------------
dstack_a_on_b:
[[[1 4]
  [2 5]
  [3 6]]]
"""
