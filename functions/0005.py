def square(x):
    return x * x

def increment_then_square(x):
    x = x + 1
    return square(x)

x = 2
print("result:", increment_then_square(x))

"""
result: 9
"""
