from sympy import Matrix , pprint
#pprint means pretty print

A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

A = Matrix(A)

print("A.row(0):")
pprint(A.row(0))
print()
print("A.row(1):")
pprint(A.row(1))
print()
print("A.row(2):")
pprint(A.row(2))


"""
A.row(0):
[1  2  3]

A.row(1):
[4  5  6]

A.row(2):
[7  8  9]
"""
