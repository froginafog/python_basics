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

print("students:")
print()

for student in data["students"]: #'student' is of the type 'dict', "students" is the key 
    print("first name:", student["first_name"]) 
    print("last name:", student["last_name"])
    print("age:", student["age"])
    print("email:", student["email"])
    print("department:", student["department"])
    print("courses:", end = " ")
    for course in student["courses"]:
        print(course, end = " ")
    print()
    print("--------------------------------------")

print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

print("teachers:")
print()

for teacher in data["teachers"]: #'student' is of the type 'dict', "teachers" is the key 
    print("first name:", teacher["first_name"])
    print("last name:", teacher["last_name"])
    print("age:", teacher["age"])
    print("email:", teacher["email"])
    print("department:", teacher["department"])
    print("courses:", end = " ")
    for course in teacher["courses"]:
        print(course, end = " ")
    print()
    print("--------------------------------------")


"""
students:

first name: Bob
last name: The Great
age: 22
email: BobTheGreat@Whatever.com
department: Physics
courses: Mechanics Electricity Optics 
--------------------------------------
first name: Robin
last name: The Hood
age: 33
email: RobinTheHood@Whatever.com
department: Engineering
courses: Programming Vectors Circuits 
--------------------------------------
first name: Mimi
last name: The Mighty
age: 44
email: MimiTheMighty@Whatever.com
department: Mathematics
courses: Probability Algebra Calculus 
--------------------------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

teachers:

first name: Celine
last name: The Dream
age: 55
email: CelineTheDream@Whatever.com
department: Physics
courses: Optics Thermodynamics 
--------------------------------------
first name: Andy
last name: The Candy
age: 66
email: AndyTheCandy@Whatever.com
department: Engineering
courses: Statics Dynamics 
--------------------------------------
first name: Tim
last name: The Beam
age: 77
email: TimTheBeam@Whatever.com
department: Mathematics
courses: Calculus Analysis 
--------------------------------------
"""
