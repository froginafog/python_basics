# The filter() function returns an iterator were
# the items are filtered through a function to test
# if the item is accepted or not.

def isAdultAge(age):
    if age >= 18:
        return True
    else:
        return False

ages = [1, 13, 18, 33, 49, 7]

adultAges = filter(isAdultAge, ages)

print("adultAges:", end = " ")
# We have to use an iterator in this case.
for currentAge in adultAges:
    print(currentAge, end = " ") 

"""
adultAges: 18 33 49
"""
