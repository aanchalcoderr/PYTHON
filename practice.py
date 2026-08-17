class University:
    def display(self):
        print("display university name")
class Course(University):
    def display(self):
        print("display course name")
class Branch(University):
    def display(self):
        print("display from branch")
class Student(Course,Branch):
    def display(self):
        print("student class")
class Faculty(Branch):
    def display(self):
        print("Faculty class")

s1=Student