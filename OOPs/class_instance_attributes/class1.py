class Person:
    count = 0
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count +=1
        
person1 = Person("Ayan", 25)
person2 = Person("Bobby", 30)
print(Person.count)