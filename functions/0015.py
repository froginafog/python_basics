def print_dictionary(**args):
    #args is a dict (dictionary)
    for key in args: #for each key in the dictionary, do
        print(key + ": " + str(args[key]))

#print_dictionary(key_1 = value_1, key_2 = value_2, ...)
print_dictionary(first_name = "Bob", last_name = "The Great", age = 33)

"""
first_name: Bob
last_name: The Great
age: 33
"""
