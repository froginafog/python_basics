#A variable created outside of a function
#is global. It can be seen inside the function.

def f():
    print(x)

x = 5

f()

"""
5
"""
