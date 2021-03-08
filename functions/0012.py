def f(x):
    result = a * x
    print("f(x):", result)

def g(x):
    result = b * x
    print("g(x):", result)

def global_variables(): #change the value of global variables
    global a
    global b
    a = 2
    b = 3

global_variables()
f(2)
g(2)

"""
f(x): 4
g(x): 6
"""
