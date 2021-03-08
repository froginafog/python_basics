# The divmod() function returns a tuple containing the quotient
# and the remainder when argument1 (dividend) is divided by argument2 (divisor).

a = 7 # dividend
d = 2 # divisor
print("a:", a)
print("d:", d)
v = divmod(a, d) 
print("v:", v)
q = v[0] # quotient
r = v[1] # remainder
print("q:", q)
print("r:", r)

# a/d = q + r/d
print(str(a) + "/" + str(d) + " = " + str(q) + " + " + str(r) + "/" + str(d))

"""
a: 7
d: 2
v: (3, 1)
q: 3
r: 1
7/2 = 3 + 1/2
"""
