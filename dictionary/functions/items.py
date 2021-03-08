#dictionary_name.items() returns a list of tuples.
#Each tuple consists of a pair of key and value associated with that key.
#Properties of a tuple: ordered, unchangeable.

person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 22,
          "programming": ["C", "Java", "PHP"]
         }

print("person.items():", person.items())

print("-----------------------------------------")

for key, value in person.items():
    print(key, ":", value)
    if(type(value) == list):
        num_elements = len(value)
        for i in range(0, num_elements):
            print(value[i])
        print()

  
"""
person.items(): dict_items([('first_name', 'Bob'), ('last_name', 'The Great'), ('age', 22), ('programming', ['C', 'Java', 'PHP'])])
-----------------------------------------
first_name : Bob
last_name : The Great
age : 22
programming : ['C', 'Java', 'PHP']
C
Java
PHP
"""
