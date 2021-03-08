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

print("people.values():", people.values())

print("------------------------------------------")

for value in people.values():
    print("first_name:", value["first_name"])
    print("last_name:", value["last_name"])
    print("age:", value["age"])
    print("--------------------------------------")

  
"""
people.values(): dict_values([{'first_name': 'Bob', 'last_name': 'The Great', 'age': 22}, {'first_name': 'Robin', 'last_name': 'The Hood', 'age': 33}, {'first_name': 'Mimi', 'last_name': 'The Mighty', 'age': 44}])
------------------------------------------
first_name: Bob
last_name: The Great
age: 22
--------------------------------------
first_name: Robin
last_name: The Hood
age: 33
--------------------------------------
first_name: Mimi
last_name: The Mighty
age: 44
--------------------------------------
"""
