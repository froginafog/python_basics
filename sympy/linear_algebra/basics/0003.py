from sympy import Matrix , pprint

A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

A = Matrix(A)

print("A.col(0):")
pprint(A.col(0))
print()
print("A.column(1):")
pprint(A.col(1))
print()
print("A.col(2):")
pprint(A.col(2))


"""
A.col(0):
⎡1⎤
⎢ ⎥
⎢4⎥
⎢ ⎥
⎣7⎦

A.column(1):
⎡2⎤
⎢ ⎥
⎢5⎥
⎢ ⎥
⎣8⎦

A.col(2):
⎡3⎤
⎢ ⎥
⎢6⎥
⎢ ⎥
⎣9⎦
"""
