person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

print("values:")
for key in person:
    print(person[key])
  
"""
values:
Bob
The Great
33
['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP']
"""
