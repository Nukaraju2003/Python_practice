class Student:
    def __init__(self):
        print("This is non parameterized constructor")
    def show(self, name):
        print("Hello", name)
s1 = Student()
s1.show("John")        