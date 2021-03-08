#dictionary_name.keys() returns a list containing the dictionary's keys

person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

print("person.keys():", person.keys())
print("----------------------------")
for key in person.keys():
    print(key)

"""
person.keys(): dict_keys(['first_name', 'last_name', 'age', 'programming'])
----------------------------
first_name
last_name
age
programming
"""
