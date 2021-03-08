person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }

person["weight"] = 123 #add an item to the dictionary
person.update({"height": 178}) #add an item to the dictionary

print("person:")
print(person)

print("-----------------------------------------------")

print("person[\"weight\"]:", person["weight"])
print("person[\"height\"]:", person["height"])
  
"""
person:
{'first_name': 'Bob', 'last_name': 'The Great', 'age': 33, 'programming': ['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP'], 'weight': 123, 'height': 178}
-----------------------------------------------
person["weight"]: 123
person["height"]: 178
"""
