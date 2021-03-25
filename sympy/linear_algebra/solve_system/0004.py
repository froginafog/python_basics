from sympy import Matrix, pprint, linsolve, Symbol, Eq

"""
solve Ax = b

example

 1 * x_1 - 2 * x_2 + 3 * x_3 = 7
 2 * x_1 + 1 * x_2 + 1 * x_3 = 4
-3 * x_1 + 2 * x_2 - 2 * x_3 = -10
"""

x_1 = Symbol('x_1')
x_2 = Symbol('x_2')
x_3 = Symbol('x_3')

eq_1 = Eq(1 * x_1 - 2 * x_2 + 3 * x_3, 7)
eq_2 = Eq(2 * x_1 + 1 * x_2 + 1 * x_3, 4)
eq_3 = Eq(-3 * x_1 + 2 * x_2 - 2 * x_3, -10)

x = linsolve([eq_1, eq_2, eq_3], (x_1, x_2, x_3))
#x = {[x_1, x_2, x_3]}
#The type of x is <class 'sympy.sets.sets.FiniteSet'>

x = list(x) #convert to list

x = x[0] #the first set of the list is the solution that we want

print("x:")
pprint(x) 

print("--------------------")

lhs_eq_1 = 1 * x_1 - 2 * x_2 + 3 * x_3
lhs_eq_2 = 2 * x_1 + 1 * x_2 + 1 * x_3
lhs_eq_3 = -3 * x_1 + 2 * x_2 - 2 * x_3

lhs_eq_1_value = lhs_eq_1.subs({x_1: x[0], x_2: x[1], x_3: x[2]})
lhs_eq_2_value = lhs_eq_2.subs({x_1: x[0], x_2: x[1], x_3: x[2]})
lhs_eq_3_value = lhs_eq_3.subs({x_1: x[0], x_2: x[1], x_3: x[2]})

print("lhs_eq_1_value:", lhs_eq_1_value)
print("lhs_eq_2_value:", lhs_eq_2_value)
print("lhs_eq_3_value:", lhs_eq_3_value)

print()

rhs_eq_1_value = 7
rhs_eq_2_value = 4
rhs_eq_3_value = -10

print("rhs_eq_1_value:", rhs_eq_1_value)
print("rhs_eq_2_value:", rhs_eq_2_value)
print("rhs_eq_3_value:", rhs_eq_3_value)

print("--------------------")

if(lhs_eq_1_value == rhs_eq_1_value
   and lhs_eq_2_value == rhs_eq_2_value
   and lhs_eq_3_value == rhs_eq_3_value):
    print("The solution " + str(x) + " is correct.")
else:
    print("The solution " + str(x) + " is incorrect.")

"""
x:
(2, -1, 1)
--------------------
lhs_eq_1_value: 7
lhs_eq_2_value: 4
lhs_eq_3_value: -10

rhs_eq_1_value: 7
rhs_eq_2_value: 4
rhs_eq_3_value: -10
--------------------
The solution (2, -1, 1) is correct.
"""
