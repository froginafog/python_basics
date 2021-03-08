#dictionary_name.popitem() pops out the last item of the dictionary

person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

popped_item = person.popitem() #pops out the last item of the dictionary
print(popped_item, "was removed from the dictionary")  
print("person:")
print(person)
  
"""
('programming', ['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP']) was removed from the dictionary
person:
{'first_name': 'Bob', 'last_name': 'The Great', 'age': 33}
"""
