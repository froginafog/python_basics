"""
n! = n * (n - 1)! = n * (n - 1) * (n - 2)! = ...
5! = 5 * 4! = 5 * 4 * 3! = 5 * 4 * 3 * 2! = 5 * 4 * 3 * 2 * 1! = 5 * 4 * 3 * 2 * 1 = 120
"""

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)
    
print(5, "! =", factorial(5))

"""
5 ! = 120
"""
