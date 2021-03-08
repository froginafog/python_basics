person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

popped_item = person.pop("programming")
print(popped_item, "was removed from the dictionary")  #pops out the specified item from the dictionary
print("person:")
print(person)
  
"""
['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP'] was removed from the dictionary
person:
{'first_name': 'Bob', 'last_name': 'The Great', 'age': 33}
"""
