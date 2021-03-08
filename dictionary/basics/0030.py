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

print("people.keys():", people.keys())

print("-----------------------")

for key in people.keys(): 
    print(key + ":")
    print("first_name:", people[key]["first_name"])
    print("last_name :", people[key]["last_name"])
    print("age       :", people[key]["age"])
    print("-----------------------")

  
"""
people.keys(): dict_keys(['person1', 'person2', 'person3'])
-----------------------
person1:
first_name: Bob
last_name : The Great
age       : 22
-----------------------
person2:
first_name: Robin
last_name : The Hood
age       : 33
-----------------------
person3:
first_name: Mimi
last_name : The Mighty
age       : 44
-----------------------
"""
