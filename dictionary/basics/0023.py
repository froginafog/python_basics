person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

#twin = person  ERROR
#copy 'person' into 'twin'
twin = person.copy()

print("twin:")
print(twin)
  
"""
twin:
{'first_name': 'Bob', 'last_name': 'The Great', 'age': 33, 'programming': ['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP']}
"""
