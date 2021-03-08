# input() is to read an input from the keyboard
# this input is stored as a string by default

print("Enter the first name:", end = " ")
firstName = input()
print("Enter the last name :", end = " ")
lastName = input()
print("Full name           :", firstName + " " + lastName)
print("-----------------------")
print("Enter a number:", end = " ")
n1 = input()
n1 = float(n1)
print("Enter another number:", end = " ")
n2 = input()
n2 = float(n2)
total = n1 + n2
print("total: %f" %total) 


"""
Enter the first name: Bob
Enter the last name : The Great
Full name           : Bob The Great
-----------------------
Enter a number: 3
Enter another number: 5
total: 8.000000
"""
