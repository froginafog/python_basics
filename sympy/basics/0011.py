from sympy import symbols

coefficients = symbols("a:5")
print("coefficients:", coefficients)
print("----------------------------")
num_coefficients = len(coefficients)
for i in range(0, num_coefficients ):
    print(coefficients[i], end = " ")
print()

"""
coefficients: (a0, a1, a2, a3, a4)
----------------------------
a0 a1 a2 a3 a4 
"""
