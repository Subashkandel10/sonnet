from model.Customer import Customer
from model.Manager import Manager
from model.exception.UnauthorizedAccessException import UnauthorizedAccessException
from model.exception.InvalidOperationException import InvalidOperationException

class Users:
    def __init__(self):
        self.users = []
    
    def add(self, user):
        self.users.append(user)

    def get_users(self):
        return self.users
    
    def insert_seed_data(self, seed_animals):
        self.add(Customer("1", "1"))
        self.add(Manager("David Dyer", 12345))
        self.add(Manager("Rishik Sood", 48954))

        self.add(Customer("Dahyun Kim", "dahyun@twice.com"))
        self.add(Customer("Zyzz", "Aziz@gains.net"))

        daisy = Customer("Daisy Doodles", "daisy252gmail.com")
        nimo = [animal for animal in seed_animals.get_animals() if animal.get_name() == "Nimo"][0]
        daisy.get_adopted_animals().add(nimo)
        nimo.adopt()
        self.add(daisy)

        jenny = Customer("Jenny Jenson", "jenny123@gmail.com")
        oliver = [animal for animal in seed_animals.get_animals() if animal.get_name() == "Oliver"][0]
        jenny.get_adopted_animals().add(oliver)
        oliver.adopt()
        self.add(jenny)

        return self
    
    def validate_customer(self, name, email):
        for user in self.users:
            if isinstance(user, Customer):
                if user.get_name() == name and user.get_email() == email:
                    return user
        return None
    
    def validate_manager(self, manager_id):
        real_id = 0
        try:
            real_id = int(manager_id)
        except:
            raise InvalidOperationException("Id must be an integer")
        for user in self.users:
            if isinstance(user, Manager):
                if user.get_manager_id() == real_id:
                    return user
        raise UnauthorizedAccessException("Invalid manager credentials")
