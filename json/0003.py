#How to remove some attributes from a json string.
import json

#json string
school_json = """
              {
                   "students": [
                                {
                                    "first_name": "Bob",
                                    "last_name": "The Great",
                                    "age": 22,
                                    "email": "BobTheGreat@Whatever.com",
                                    "department": "Physics",
                                    "courses": ["Mechanics", "Electricity", "Optics"]
                                },
                                {
                                    "first_name": "Robin",
                                    "last_name": "The Hood",
                                    "age": 33,
                                    "email": "RobinTheHood@Whatever.com",
                                    "department": "Engineering",
                                    "courses": ["Programming", "Vectors", "Circuits"]
                                },
                                {
                                    "first_name": "Mimi",
                                    "last_name": "The Mighty",
                                    "age": 44,
                                    "email": "MimiTheMighty@Whatever.com",
                                    "department": "Mathematics",
                                    "courses": ["Probability", "Algebra", "Calculus"]
                                }
                               ],
                   "teachers": [
                                {
                                    "first_name": "Celine",
                                    "last_name": "The Dream",
                                    "age": 55,
                                    "email": "CelineTheDream@Whatever.com",
                                    "department": "Physics",
                                    "courses": ["Optics", "Thermodynamics"]
                                },
                                {
                                    "first_name": "Andy",
                                    "last_name": "The Candy",
                                    "age": 66,
                                    "email": "AndyTheCandy@Whatever.com",
                                    "department": "Engineering",
                                    "courses": ["Statics", "Dynamics"]
                                },
                                {
                                    "first_name": "Tim",
                                    "last_name": "The Beam",
                                    "age": 77,
                                    "email": "TimTheBeam@Whatever.com",
                                    "department": "Mathematics",
                                    "courses": ["Calculus", "Analysis"]
                                }
                               ]
                    
              }
              """

#load 'school_json' into python 'data'
data = json.loads(school_json)
#'data' is of the type 'dict'

#---------------------------------------------------------------------
#Remove the 'age' and 'email' attributes from the students and teachers.

for student in data["students"]:
    del student["age"]
    del student["email"]

for teacher in data["teachers"]:
    del teacher["age"]
    del teacher["email"]

#save the modified 'data' into 'new_school_json'
new_school_json = json.dumps(data, indent = 4)
#'new_school_json' is a json string

print(new_school_json)
print()
