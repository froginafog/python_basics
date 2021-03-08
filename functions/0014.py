#functions with variable number of arguments
def add(*args):
    #args is a tuple
    total = 0
    num_args = len(args)
    for i in range(0, num_args):
        total = total + args[i]
    return total

sum_of_numbers = add(1, 2, 3, 4, 5)
print("sum_of_numbers:", sum_of_numbers)

"""
sum_of_numbers: 15
"""
