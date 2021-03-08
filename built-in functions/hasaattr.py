"""
The hasattr() function returns True if the specified object
has the specified attribute. Otherwise, it returns False otherwise.
"""

class Person:
  name = "Bob The Great"
  age = 45
  country = "Madagascar"

if(hasattr(Person, "country")):
    print("Person.country:", Person.country)
else:
    print("Person.country does not exist")

if(hasattr(Person, "city")):
    print("Person.city:", Person.city)
else:
    print("Person.city does not exist")

"""
Person.country: Madagascar
Person.city does not exist
"""
