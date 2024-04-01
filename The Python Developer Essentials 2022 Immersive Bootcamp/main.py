# print("First Line!")
# print("second line!")
# print("Third Line!")    
# fruit ="banana"
# print("The fruit is",fruit)
# fruit = "banana"
# print("The fruit is"+" "+ fruit)
# fruit1 = "banana"
# fruit2 = "fig"
# print("The fruit1 is",fruit1,"and the fruit2 is",fruit2)
# x = 1
# y = -5.2
# numbers = [1,2,3]
# fruit = "fig"
# print(type(x))
# print(type(y))
# print(type(fruit))
# print(type(numbers))
# print(type(0xFF))
#print(9%3)
# op = 10 + ((10*2)/3) - 3
# print(op)
# print(17%5)
# d1 ={"name": "ronaldo"}
# print(d1["name"])

# def addNumbers(x):
#     result = x + x
#     return  result
# print(addNumbers(5))

#Get the type
# x= 1
# print(type(x))

#Get an input
# name = input("what's your name?")
# print("Your name is",name)

# x= 10.1
# print(int(x))

# x = str(10.1)
# print(type(x))

# x= float(10)
# print(type(x))

# x = float(10)
# print(x)

# def multiplyFunc(x):
#     result = x*x
#     return result
# print(multiplyFunc(5))    # 25
# print(multiplyFunc(6))    # 36

# def multiplyFunc(x,y):
#     result = x*y
#     return result
# print(multiplyFunc(5,6))    # 30

# def multiplyFunc(x,y):
#     multiply = x*y
#     sum = x+y
#     divide = x/y 
#     return multiply, sum, divide
# print(multiplyFunc(5,6))                 #(30, 11, 0.8333333333333334)

#lambda anonymous     
# x= lambda i: i + 11
# print(x(5))   # 16
# print(x(6))   # 17

# x= lambda i, y, z: i + y + z  
# print(x(5,3,2))   # 10
# print(x(6,4,1))   # 11

# def new(i):
#     return lambda x : x * i
# double = new(2)
# triple = new(3)

# print(double(5))   # 10
# print(triple(5))   # 15

# def new():
#     x = 20
#     print(x)
# new()            # 20


# x= 10
# def new():
#     x=20
#     print(x)
# new()
# print(x)       # 20 #10


# def new():
#     global x 
#     x= 20
#     print(x)
# new()
# print(x)    #20 #20

# colors = ["Red", "Orange","Yellow", "Red"]
# colors.append("purple")
# print(colors)

# colors = ["Red", "Orange","Yellow", "Red"]
# newcolors = ["purple","blue"]
# colors.extend(newcolors)
# print(colors)

# fruits = ("fig","banana","lemon")
# print(fruits[:2])

# integers1 =(1,2,3)
# integers2 =(4,5,6)
# del integers1
# print(integers1)

# fruits1 = {}
# print(type(fruits1))

# fruits2 = set(())
# print(type(fruits2))
# fruits = {"orange","fig","Cherry"}
# del fruits
# print(fruits)

'''dictionaries'''
# person = {
#     "name" : "fred",
#     "age" : 30,
#     "country" : "Germany"
# }
# person.clear()
# print(person)
# person.update({"id":21, "number": 50})
# print(person)

# x = 2
# # y = 4
# print(not(x<3 and x<9))

# list1 = ["fig", "apple"]
# list2 = ["fig", "apple"]
# list3 = list2
# print("banana" not in list1)

# x = 22
# # y= 100
# # if y < x:
# #     print("This is True, y is not greater than x!")
# # elif y == x:
# #     print("This is True, y is greater than x!")
# # else:
# #     print("Anything else!")    
# # print("Completed")    

# x= 1
# while x < 7:
#     x= x+1
#     if x ==3:
#         continue
#     print(x)
# else:
#     print("x is longer less than 7!")    

# fruits = ["banana","apple","orange"]
# for item in fruits:
#     print(item)


# fruit ="banana"
# for x in fruit:
#     if x == "n":
#         continue
#     print(x)

# for x in range(3,15, 3):
#     print(x)
# else:
#     print("completed")    

# class Person:
#     """Create a new Person"""
#     def __init__(self, fname,lname):
#         self.fname = fname
#         self.lname = lname
        
# newPerson = Person("Dony", "Beckar")

# newPerson.fname = "cris"
# newPerson.lname = "Ronaldo"
# #Displaying the output
# del newPerson
# print(newPerson)


# class Person:
#     """Create a new Person"""
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def new(self):
#         print("Hi, my name is "+ self.fname)    
#         print("Hi, my name is "+ self.lname)  
# newPerson = Person("Dony","Becker")
# aothername = Person("first", "last")

# newPerson.new() 
# aothername.new()       

# class Player:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
# class NewPlayer(Player):
    
#     def __init__(self, fname, lname, total):
#         Player.__init__(self, fname, lname)
#         self.total = total
        
#     def getDetails(self):
#         return "%s %s has spent %s in total" %(self.fname, self.lname, self.total)
                
# newP = NewPlayer("Dony", "Becker", 1000)     
# print(newP.getDetails())           

# import platform
# op = dir(platform)
# print(op)

# import math

# print(math.log(10))

# file = open("main.txt", "r")
# print(file.readline())
# print(file.readline())

# file = open("main.txt", "r")
# for x in file:
#     print(x)

# file = open("main.txt", "r")
# print(file.read(10))
# file.close()

# file = open("demo.txt", "w")

import os
os.remove("demo.txt")