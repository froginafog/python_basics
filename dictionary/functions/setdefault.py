#dictionary_name.setdefault(key, value) returns the value of the item with the specified key
#The second argument is optional.
#If the key does not exist, then the key is inserted with some value.

person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

print("person:")
print(person)

print("--------------1--------------")

value = person.setdefault("age") 
print("value:")
print(value)

print("--------------2--------------")

value = person.setdefault("weight", 150)
print("value:")
print(value)

print("--------------3--------------")

print("person:")
print(person)

"""
person:
{'first_name': 'Bob', 'last_name': 'The Great', 'age': 33, 'programming': ['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP']}
--------------1--------------
value:
33
--------------2--------------
value:
150
--------------3--------------
person:
{'first_name': 'Bob', 'last_name': 'The Great', 'age': 33, 'programming': ['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP'], 'weight': 150}
"""
