person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

del person["programming"] #deletes the specified item from the dictionary
print("person:")
print(person)
  
"""
person:
{'first_name': 'Bob', 'last_name': 'The Great', 'age': 33}
"""
