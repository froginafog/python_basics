import json

#json data frame
person_json = """
              {                                            
                  "first_name": "Bob",                       
                  "last_name": "The Great",                  
                  "age": 30,                                 
                  "programming": ["C", "C++", "Python"]      
              }
              """
#'person' is a string

person_dict = json.loads(person_json)
#parse the json string into a dictionary

print(person_dict)
