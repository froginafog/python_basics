person_1 = {"first_name": "Bob",
            "last_name": "The Great",
            "age": 22
           }

person_2 = {"first_name": "Robin",
            "last_name": "The Hood",
            "age": 33
           }

person_3 = {"first_name": "Mimi",
            "last_name": "The Mighty",
            "age": 44
           }

#nested dictionarys:
people = {"person1": person_1,
          "person2": person_2,
          "person3": person_3
         }

print(people)
  
"""
{'person1': {'first_name': 'Bob', 'last_name': 'The Great', 'age': 22}, 'person2': {'first_name': 'Robin', 'last_name': 'The Hood', 'age': 33}, 'person3': {'first_name': 'Mimi', 'last_name': 'The Mighty', 'age': 44}}
"""
