"""
The "self" parameter is a reference to the current instance of the class.
It is used to access variables that belongs to the class.
It is an object.
The label "self" is arbitrarily chosen, it could be something else.
"""

class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def printInfo(self): #We must put "self" in the argument of the function.
        print("self.firstName:", self.firstName)
        print("self.lastName :", self.lastName)
        print("self.age      :", self.age)

#The label "self" in the argument of the function is arbitrarily chosen.
#The label could be something else.

person1 = Person("Bob", "The Great", 21)
person2 = Person("Kate", "The Best", 63)
person1.printInfo()
print()
person2.printInfo()

"""
self.firstName: Bob
self.lastName : The Great
self.age      : 21

self.firstName: Kate
self.lastName : The Best
self.age      : 63
"""
