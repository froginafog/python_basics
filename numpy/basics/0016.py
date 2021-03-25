import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

stack_a_on_b = np.stack((a,b)) 
print("stack_a_on_b :")
print(stack_a_on_b )

print("------------------------------")

stack_a_on_b_with_axis_0 = np.stack((a,b), axis = 0)
print("stack_a_on_b_with_axis_0:")
print(stack_a_on_b_with_axis_0)
print(stack_a_on_b_with_axis_0)

print("------------------------------")

stack_a_on_b_with_axis_1 = np.stack((a,b), axis = 1)
print("stack_a_on_b_with_axis_1:")
print(stack_a_on_b_with_axis_1)
print(stack_a_on_b_with_axis_1)

"""
stack_a_on_b :
[[1 2 3]
 [4 5 6]]
------------------------------
stack_a_on_b_with_axis_0:
[[1 2 3]
 [4 5 6]]
[[1 2 3]
 [4 5 6]]
------------------------------
stack_a_on_b_with_axis_1:
[[1 4]
 [2 5]
 [3 6]]
[[1 4]
 [2 5]
 [3 6]]
"""
