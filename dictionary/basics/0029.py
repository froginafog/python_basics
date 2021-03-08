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

print("person1:")
print(people["person1"]["first_name"])
print(people["person1"]["last_name"])
print(people["person1"]["age"])
print("-----------------------")
print("person2:")
print(people["person2"]["first_name"])
print(people["person2"]["last_name"])
print(people["person2"]["age"])
print("-----------------------")
print("person3:")
print(people["person3"]["first_name"])
print(people["person3"]["last_name"])
print(people["person3"]["age"])
  
"""
person1:
Bob
The Great
22
-----------------------
person2:
Robin
The Hood
33
-----------------------
person3:
Mimi
The Mighty
44
"""
