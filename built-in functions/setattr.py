#The setattr() function sets the value of the specified attribute of the specified object.
#setattr(className, variableName, newValue)

class Person:
    firstName = "Bob"
    lastName = "The Great"
    age = 32

setattr(Person, 'age', 43)

print(Person.firstName)
print(Person.lastName)
print(Person.age)

"""
Bob
The Great
43
"""
