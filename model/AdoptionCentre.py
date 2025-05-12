from model.Users import Users
from model.Animals import Animals

class AdoptionCentre:
    logged_in_user = None
    def __init__(self):
        self.animals = seed_animals = Animals().insert_seed_data()
        self.users = Users().insert_seed_data(seed_animals)
    
    def get_users(self):
        return self.users

    def get_adoptable_animals(self):
        return [animal for animal in self.animals.get_animals() if not animal.is_already_adopted()]