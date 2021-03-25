from sympy import ask, Q

print("ask(Q.positive(-3)):", ask(Q.positive(-3)))
print("ask(Q.positive(3)):", ask(Q.positive(3)))
print("ask(Q.negative(-3)):", ask(Q.negative(-3)))
print("ask(Q.negative(3)):", ask(Q.negative(3)))

"""
ask(Q.positive(-3)): False
ask(Q.positive(3)): True
ask(Q.negative(-3)): True
ask(Q.negative(3)): False
"""
