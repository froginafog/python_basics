person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

sought_key = "age"
if sought_key in person:
  print(sought_key + " is a key in the dictionary called person")
else:
  print(sought_key + " is not a key in the dictionary called person")

print("----------------------------------------------------------------")

sought_key = "height"
if sought_key in person:
  print(sought_key + " is a key in the dictionary called person")
else:
  print(sought_key + " is not a key in the dictionary called person")
  
"""
age is a key in the dictionary called person
----------------------------------------------------------------
height is not a key in the dictionary called person
"""
