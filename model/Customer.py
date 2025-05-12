from model.User import User
from model.Animals import Animals

class Customer(User):
    ADOPTION_LIMIT = 2
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
        self.adopted_animals = Animals()
    
    def get_adopted_animals(self):
        return self.adopted_animals
    
    def get_email(self):
        return self.email

    def can_adopt(self, animal):
        count = 0
        for a in self.adopted_animals.get_animals():
            if type(a) == type(animal):
                count = count + 1
        return count < Customer.ADOPTION_LIMIT

    def __str__(self):
        return f"{self.name} ({self.email})"