from sympy import Rational

print("Rational(3/4):", Rational(3/4))
print("Rational(9/3):", Rational(9/3))
print("Rational(0.5):", Rational(0.5))
print("---------------------------------------------")
print("Rational(0.2):", Rational(0.2))
print("Rational(0.2).limit_denominator(100):", Rational(0.2).limit_denominator(100))
print("---------------------------------------------")
print("Rational(\"0.5\"):", Rational("0.5"))
print("Rational(\"0.2\"):", Rational("0.2"))
print("---------------------------------------------")
print("Rational(3, 4):", Rational(3, 4)) #Rational(numerator, denominator)
print("Rational(9, 3):", Rational(9, 3))

#When using rational, it is better to convert the number into a string first. 

"""
Rational(3/4): 3/4
Rational(9/3): 3
Rational(0.5): 1/2
---------------------------------------------
Rational(0.2): 3602879701896397/18014398509481984
Rational(0.2).limit_denominator(100): 1/5
---------------------------------------------
Rational("0.5"): 1/2
Rational("0.2"): 1/5
---------------------------------------------
Rational(3, 4): 3/4
Rational(9, 3): 3
"""
