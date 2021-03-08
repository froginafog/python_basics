#dictionary items are: ordered, changeable, unique

person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33
         }

#print("person[0]:",person[0])  ERROR
#print("person[1]:",person[1])  ERROR
#print("person[2]:",person[2])  ERROR

print("person[\"first_name\"]:", person["first_name"])  
print("person[\"last_name\"]:", person["last_name"])  
print("person[\"age\"]:", person["age"]) 

"""
person["first_name"]: Bob
person["last_name"]: The Great
person["age"]: 33
"""
