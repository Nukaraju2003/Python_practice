class MyClass:
    def __init__(self, value):
        self.value = value
    
    def my_method(self, increment):
        self.value +=increment
        return self.value
    
obj = MyClass(5)
result = obj.my_method(3)
print(result)