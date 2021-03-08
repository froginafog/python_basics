#dictionary items are: ordered, changeable, unique

person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

keys = person.keys()
print("keys:", keys)
print("----------------------------------------------------------")
values = person.values()
print("values:", values)


"""
keys: dict_keys(['first_name', 'last_name', 'age', 'programming'])
----------------------------------------------------------
values: dict_values(['Bob', 'The Great', 33, ['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP']])
"""
