from model.User import User

class Manager(User):
    def __init__(self, name, manager_id):
        super().__init__(name)
        self.manager_id = manager_id

    def get_manager_id(self):
        return self.manager_id

    def __str__(self):
        return f"{self.name} (Manager)"