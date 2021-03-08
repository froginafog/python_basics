# The getattr() function returns the value of the specified attribute
# from the specified object.

class Person:
  name = "Bob The Great"
  age = 54
  country = "Madagascar"

countryName = getattr(Person, 'country')
print("countryName:", countryName)

"""
countryName: Madagascar
"""
