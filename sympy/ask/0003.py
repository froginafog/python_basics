from sympy import ask, Q

print("ask(Q.integer(3)):", ask(Q.integer(3)))
print("ask(Q.integer(3.14)):", ask(Q.integer(3.14)))

"""
ask(Q.integerl(3)): True
ask(Q.integer(3.14)): False
"""
