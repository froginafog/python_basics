#dictionary items are: ordered, changeable, unique

person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "age": 44
         }

#duplicate keys will overwrite existing values

print("person[\"first_name\"]:", person["first_name"])  
print("person[\"last_name\"]:", person["last_name"])  
print("person[\"age\"]:", person["age"]) 

"""
person["first_name"]: Bob
person["last_name"]: The Great
person["age"]: 44
"""
