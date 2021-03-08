person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

#The items() method returns a list of tuples.
#Each tuple consists of a pair of key and value associated with that key.
#Properties of a tuple: ordered, unchangeable.

items = person.items()
print("items:")
print(items)

"""
items:
dict_items([('first_name', 'Bob'), ('last_name', 'The Great'), ('age', 33), ('programming', ['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP'])])
"""
