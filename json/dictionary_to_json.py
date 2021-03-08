import json

person_dict = {                                            
                "first_name": "Bob",                       
                "last_name": "The Great",                  
                "age": 30,                                 
                "programming": ["C", "C++", "Python"]      
              }

#'person_dict' is a dictionary

person_json = json.dumps(person_dict, indent = 4, sort_keys = False)
#'person_json' is a json string

print(person_json)

