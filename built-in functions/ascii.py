# The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc).
# The ascii() function will replace any non-ascii characters with escape characters:
# The escape character: \xe5
s = "Whåles are great."
print("s:", s)
s = ascii("Whåles are great.")
print("s:", s)

"""
s: Whåles are great.
s: 'Wh\xe5les are great.'
"""
