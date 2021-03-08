#dictionary items are: ordered, changeable, unique

person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 33,
          "age": 44
         }

#duplicate keys will overwrite existing values

num_keys = len(person) 
print("num_keys:", num_keys)
#duplicate keys are not counted

"""
num_keys: 3
"""
