person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

print("key: values")
for key in person:
    print(key + ": " + str(person[key]))
  
"""
key: values
first_name: Bob
last_name: The Great
age: 33
programming: ['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP']
"""
