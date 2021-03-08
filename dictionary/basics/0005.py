#dictionary items are: ordered, changeable, unique

person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "programming": ["C", "C++", "Java", "Python", "Javascript", "PHP"]
         }


print("person[\"first_name\"]:", person["first_name"])
print("person[\"last_name\"]:", person["first_name"])
print("person[\"age\"]:", person["first_name"])
print("person[\"programming\"]:", person["programming"])
print("-------------------------------------------------------")
print("person[\"programming\"][0]:", person["programming"][0])
print("person[\"programming\"][1]:", person["programming"][1])
print("person[\"programming\"][2]:", person["programming"][2])
print("person[\"programming\"][3]:", person["programming"][3])
print("person[\"programming\"][4]:", person["programming"][4])
print("person[\"programming\"][5]:", person["programming"][5])

"""
person["first_name"]: Bob
person["last_name"]: Bob
person["age"]: Bob
person["programming"]: ['C', 'C++', 'Java', 'Python', 'Javascript', 'PHP']
-------------------------------------------------------
person["programming"][0]: C
person["programming"][1]: C++
person["programming"][2]: Java
person["programming"][3]: Python
person["programming"][4]: Javascript
person["programming"][5]: PHP
"""
