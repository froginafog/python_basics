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
                               ]
              }
              """

#load 'school_json' into python 'data'
data = json.loads(school_json)
#'data' is of the type 'dict'

print("students:")
print()

for student in data["students"]: #'student' is of the type 'dict', "students" is the key 
    print("first name:", student["first_name"]) #"first_name" is the key, person["first_name"] is the value
    print("last name:", student["last_name"])
    print("age:", student["age"])
    print("email:", student["email"])
    print("department:", student["department"])
    print("courses:", end = " ")
    for course in student["courses"]:
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
"""
