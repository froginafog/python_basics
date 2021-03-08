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

print("people[\"person1\"]:", people["person1"])
print("people[\"person2\"]:", people["person2"])
print("people[\"person3\"]:", people["person3"])
  
"""
people["person1"]: {'first_name': 'Bob', 'last_name': 'The Great', 'age': 22}
people["person2"]: {'first_name': 'Robin', 'last_name': 'The Hood', 'age': 33}
people["person3"]: {'first_name': 'Mimi', 'last_name': 'The Mighty', 'age': 44}
"""
