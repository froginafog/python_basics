class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def print_first_name(self):
        print(self.first_name, end = "")

    def print_last_name(self):
        print(self.last_name, end = "")

class Student(Person):
    def __init__(self, first_name, last_name, ID, program, gpa):
        Person.__init__(self, first_name, last_name)
        self.ID = ID
        self.program = program
        self.gpa = gpa

    def print_ID(self):
        print(self.ID, end = "")

    def print_program(self):
        print(self.program, end = "")

    def print_gpa(self):
        print(self.gpa, end = "")
    
student1 = Student("Bob", "The Great", "B123", "Chemistry", 2.13)
student2 = Student("Robin", "The Hood", "R123", "Physics", 3.51)

print("student1:")
student1.print_first_name()
print()
student1.print_last_name()
print()
student1.print_ID()
print()
student1.print_program()
print()
student1.print_gpa()
print()

print("----------------------------")

print("student2:")
student2.print_first_name()
print()
student2.print_last_name()
print()
student2.print_ID()
print()
student2.print_program()
print()
student2.print_gpa()
print()

"""
student1:
Bob
The Great
B123
Chemistry
2.13
----------------------------
student2:
Robin
The Hood
R123
Physics
3.51
"""
