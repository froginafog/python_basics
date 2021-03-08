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

print("-----------------------------------")

person1 = Person("Bob", "The Great", 21)
person2 = Person("Kate", "The Best", 63)

#"del" is for removing an attribute from an object
del person1.age 
del person2.age

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
-----------------------------------
self.firstName: Bob
self.lastName : The Great

'Person' object has no attribute 'age'
"""
