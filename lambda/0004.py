def f(x):
    return lambda y : x + y
#this function is to multiply a known number with an uknown number
#x is known
#y is unknown

print("f(5):", f(5))

g = f(5)
g(10)

print("g(10):", g(10))

#The equivalent code is shown below.
"""
def f(x):
    def g(y):
        return x + y
    return g

g = f(5)
print("f(5):", f(5))
print("g(10):", g(10))
"""

"""
f(5): <function f.<locals>.<lambda> at 0x0330C1D8>
result: 15
"""
