#dictionary items are: ordered, changeable, unique

person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

person["age"] = 44  #change the value associated with the key "age"
print("person[\"age\"]:", person["age"])

"""
person["age"]: 44
"""
