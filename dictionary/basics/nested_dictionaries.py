person_1 = {"first_name": "Bob",
            "last_name": "The Great",
            "age": 22,
            "programming": ["C", "Java", "PHP"]
           }

person_2 = {"first_name": "Robin",
            "last_name": "The Hood",
            "age": 33,
            "programming": ["C++", "PHP", "Python"]
           }

person_3 = {"first_name": "Mimi",
            "last_name": "The Mighty",
            "age": 44,
            "programming": ["Node", "Python", "Javascript"]
           }

#nested dictionarys:
people = {"person1": person_1,
          "person2": person_2,
          "person3": person_3
         }

for people_key, people_value in people.items():
    print(people_key)
    for person_key, person_value in people_value.items():
        print(person_key, ":", person_value)
        if(type(person_value) is list): #print the list using indices
            num_elements = len(person_value)
            for i in range(0, num_elements):
                print(person_value[i], end = " ")
            print()
    print("----------------------------------")

"""
person1
first_name : Bob
last_name : The Great
age : 22
programming : ['C', 'Java', 'PHP']
C Java PHP 
----------------------------------
person2
first_name : Robin
last_name : The Hood
age : 33
programming : ['C++', 'PHP', 'Python']
C++ PHP Python 
----------------------------------
person3
first_name : Mimi
last_name : The Mighty
age : 44
programming : ['Node', 'Python', 'Javascript']
Node Python Javascript 
----------------------------------
"""

