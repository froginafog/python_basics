#The super() function is used to give access to methods
#and properties of a parent or sibling class.
#The super() function returns an object that represents the parent class.

#The following code creates a class that will inherit all the methods
#and properties from another class.

#parent class
class Person:
  def __init__(self, name):
    self.name = name

  def printName(self):
    print(self.name)

#child class
class DoSomething(Person):
  def __init__(self, name):
    super().__init__(name)

do_something_1 = DoSomething("Bob The Great")
do_something_1.printName()

"""
Bob The Great
"""
