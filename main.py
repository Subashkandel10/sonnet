import sys
import os
import importlib.util

def import_from_file(module_name, file_path):
    """Import a module from a file path."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Import model files
Animal = import_from_file("Animal", os.path.join(current_dir, "model", "Animal.py"))
Animals = import_from_file("Animals", os.path.join(current_dir, "model", "Animals.py"))
User = import_from_file("User", os.path.join(current_dir, "model", "User.py"))
Customer = import_from_file("Customer", os.path.join(current_dir, "model", "Customer.py"))
Manager = import_from_file("Manager", os.path.join(current_dir, "model", "Manager.py"))
Users = import_from_file("Users", os.path.join(current_dir, "model", "Users.py"))
AdoptionCentre = import_from_file("AdoptionCentre", os.path.join(current_dir, "model", "AdoptionCentre.py"))

# Import exception files
InvalidOperationException = import_from_file("InvalidOperationException", 
                                          os.path.join(current_dir, "model", "exception", "InvalidOperationException.py"))
UnauthorizedAccessException = import_from_file("UnauthorizedAccessException", 
                                            os.path.join(current_dir, "model", "exception", "UnauthorizedAccessException.py"))

# Import views
Utils = import_from_file("Utils", os.path.join(current_dir, "Utils.py"))
LoginView = import_from_file("LoginView", os.path.join(current_dir, "LoginView.py"))
ManagerDashboardView = import_from_file("ManagerDashboardView", os.path.join(current_dir, "ManagerDashboardView.py"))
CustomerDashboardView = import_from_file("CustomerDashboardView", os.path.join(current_dir, "CustomerDashboardView.py"))
ErrorView = import_from_file("ErrorView", os.path.join(current_dir, "ErrorView.py"))
UserListView = import_from_file("UserListView", os.path.join(current_dir, "UserListView.py"))
AddAnimalView = import_from_file("AddAnimalView", os.path.join(current_dir, "AddAnimalView.py"))
DetailsView = import_from_file("DetailsView", os.path.join(current_dir, "DetailsView.py"))

if __name__ == "__main__":
    LoginView.LoginView() 