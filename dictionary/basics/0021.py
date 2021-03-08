person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

print("keys:")
keys = person.keys()
for key in keys :
    print(key)
print("------------------------------------")
print("values:")
values = person.values()
for value in values:
    print(value)
  
"""
keys:
first_name
last_name
age
programming
------------------------------------
values:
Bob
The Great
33
['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP']
"""
