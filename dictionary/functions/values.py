#dictionary_name.values() returns a list containing the dictionary's values

person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

print("person.values():", person.values())
print("------------------------------------------")
for value in person.values():
    print(value)

"""
person.values(): dict_values(['Bob', 'The Great', 33, ['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP']])
------------------------------------------
Bob
The Great
33
['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP']
"""
