#dictionary items are: ordered, changeable, unique

person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

keys = person.keys()
print("keys:", keys)
print("----------------------------------------------------------")
print("create new key and value")
person["weight"] = 123
keys = person.keys()
print("keys:", keys)
print("----------------------------------------------------------")
print("person[\"weight\"]:", person["weight"])

"""
keys: dict_keys(['first_name', 'last_name', 'age', 'programming'])
----------------------------------------------------------
create new key and value
keys: dict_keys(['first_name', 'last_name', 'age', 'programming', 'weight'])
----------------------------------------------------------
person["weight"]: 123
"""
