person = {"first_name": "Bob",
          "last_name": "The Great",
          "age": 22,
          "programming": ["C", "Java", "PHP"]
         }

for key, value in person.items():
    print(key, ":", value)
    if(type(value) == list):
        num_elements = len(value)
        print("programming languages:", end = " ")
        for i in range(0, num_elements):
            print(value[i], end = " ")
        print()

  
"""
first_name : Bob
last_name : The Great
age : 22
programming : ['C', 'Java', 'PHP']
programming languages: C Java PHP 
"""
