#The range() function returns a sequence of numbers,
#starting from 0 by default, and increments by 1 (by default)
#and stops before a specified number.
start = 0
stop = 10
sequence = range(start, stop)
print("sequence:", end = " ")
for n in sequence:
    print(n, end = " ")
    
print()
print("-----------------------------------")

start = 0
stop = 10
step = 2
evenNumbers = range(start, stop, step)
print("evenNumbers:", end = " ")
for n in evenNumbers:
    print(n, end = " ")

print()
print("-----------------------------------")

start = 1
stop = 10
step = 2
oddNumbers = range(start, stop, step)
print("oddNumbers:", end = " ")
for n in oddNumbers:
    print(n, end = " ")

"""
sequence: 0 1 2 3 4 5 6 7 8 9 
-----------------------------------
evenNumbers: 0 2 4 6 8 
-----------------------------------
oddNumbers: 1 3 5 7 9
"""
