from sympy import ask, Q

print("ask(Q.rational(3)):", ask(Q.rational(3)))
print("ask(Q.rational(3.14)):", ask(Q.rational(3.14)))

"""
ask(Q.rational(3)): True
ask(Q.rational(3.14)): None
"""
