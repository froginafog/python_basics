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

people_keys = people.keys()
people_values = people.values()

print("people_keys:", people_keys)
print()
print("people_values:", people_values)
  
"""
people_keys: dict_keys(['person1', 'person2', 'person3'])

people_values: dict_values([{'first_name': 'Bob', 'last_name': 'The Great', 'age': 22}, {'first_name': 'Robin', 'last_name': 'The Hood', 'age': 33}, {'first_name': 'Mimi', 'last_name': 'The Mighty', 'age': 44}])
"""
