from sympy import ask, Q

print("ask(Q.even(2)):", ask(Q.even(2)))
print("ask(Q.odd(2)):", ask(Q.odd(2)))
print("ask(Q.even(3)):", ask(Q.even(3)))
print("ask(Q.odd(3)):", ask(Q.odd(3)))
print("ask(Q.even(4)):", ask(Q.even(4)))
print("ask(Q.odd(4)):", ask(Q.odd(4)))
print("-----------------------")
print("ask(Q.prime(2)):", ask(Q.prime(2)))
print("ask(Q.prime(3)):", ask(Q.prime(3)))
print("ask(Q.prime(4)):", ask(Q.prime(4)))

"""
ask(Q.even(2)): True
ask(Q.odd(2)): False
ask(Q.even(3)): False
ask(Q.odd(3)): True
ask(Q.even(4)): True
ask(Q.odd(4)): False
-----------------------
ask(Q.prime(2)): True
ask(Q.prime(3)): True
ask(Q.prime(4)): False
"""
