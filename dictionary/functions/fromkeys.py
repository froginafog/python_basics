keys = ["first_name", "last_name", "age"]

new_dictionary_1 = dict.fromkeys(keys)
#returns a new dictionary whose keys are set according to the list 'keys'
#and whose values are set the default value 'None'

print("new_dictionary_1:")
print(new_dictionary_1)

print("----------------------------------")


values = ["Bob", "The Great", 33]

new_dictionary_2 = dict.fromkeys(keys, values)
#returns a new dictionary whose keys are set according to the list 'keys'
#and whose values are set according to the list 'values'

print("new_dictionary_2:")
print(new_dictionary_2)

"""
new_dictionary_1:
{'first_name': None, 'last_name': None, 'age': None}
----------------------------------
new_dictionary_2:
{'first_name': ['Bob', 'The Great', 33], 'last_name': ['Bob', 'The Great', 33], 'age': ['Bob', 'The Great', 33]}
"""
