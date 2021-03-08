person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

#person.items() returns a view object

for key, value in person.items():
    print(key + ": " + str(value))
  
"""
first_name: Bob
last_name: The Great
age: 33
programming: ['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP']
"""
