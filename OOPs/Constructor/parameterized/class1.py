# Constructor

# All classes have a function called _init_(), which is always executed when the class is being initiated 


# class Student:
#     name = "raju"

# s1 = Student()

# print(s1.name)

# class Student:
#     name = "raju"
#     def __init__(self):
#         print(self)
#         print("adding new student in Database..")
        
# s1 = Student()
# # print(self)
# print(s1.name)        



# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class  

class Student:
    
    #default constructors
    def __init__():
        pass 
    
    #parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")
        
s1 = Student("raju", 97)
print(s1.name, s1.marks)

s2 = Student("ram", 67)
print(s2.name, s2.marks)
        