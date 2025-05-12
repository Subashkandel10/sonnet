class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.adopted = False
    
    def get_name(self):
        return self.name
    
    def is_already_adopted(self):
        return self.adopted
    
    def adopt(self):
        self.adopted = True

    def __str__(self):
        return f"{self.name} (Age: {self.age})"

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Rabbit(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)