# index() returns the index of the first element with the selected value

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print("The value 3 is located at the position " + str(a.index(3)) + " of a[].")

print("The value 9 is located at the position " + str(b.index(9)) + " of b[].")

print("The value 123 is located at the position " + str(a.index(123)) + " of a[].")

    
"""
The value 3 is located at the position 2 of a[].
The value 9 is located at the position 3 of b[].
Traceback (most recent call last):
  File "C:/Users/wave/Desktop/Python_files/arrays/0022.py", line 22, in <module>
    print("The value 123 is located at the position " + str(a.index(123)) + " of a[].")
ValueError: 123 is not in list
"""

