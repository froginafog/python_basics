"""
The exec() function executes the specified Python code.
"""

codeBlock = 'firstName = "Bob"\nlastName = "The Great"\nprint(firstName + " " + lastName)'
exec(codeBlock)

"""
Bob The Great
"""
