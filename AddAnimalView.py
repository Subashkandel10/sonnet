from tkinter import *
from Utils import Utils
from model.Animal import Cat, Dog, Rabbit
from model.exception.InvalidOperationException import InvalidOperationException
from ErrorView import ErrorView

class AddAnimalView:
    def __init__(self, animals, callback):
        self.animals = animals
        self.callback = callback  # Callback to refresh the animals list
        self.window = Utils.top_level("Add Animal")
        self.setup_ui()
        self.window.grab_set()  # Make window modal
    
    def setup_ui(self):
        main_frame = Utils.frame(self.window)
        main_frame.pack(padx=20, pady=20)
        
        # Title
        title_label = Utils.label(main_frame, "Add Animal")
        title_label.pack(pady=10)
        
        # Name field
        name_frame = Frame(main_frame)
        name_frame.pack(fill=X, pady=5)
        
        name_label = Label(name_frame, text="Name:")
        name_label.pack(side=LEFT)
        
        self.name_entry = Entry(name_frame)
        self.name_entry.pack(side=RIGHT, expand=True, fill=X)
        
        # Age field
        age_frame = Frame(main_frame)
        age_frame.pack(fill=X, pady=5)
        
        age_label = Label(age_frame, text="Age:")
        age_label.pack(side=LEFT)
        
        self.age_entry = Entry(age_frame)
        self.age_entry.pack(side=RIGHT, expand=True, fill=X)
        
        # Type dropdown
        type_frame = Frame(main_frame)
        type_frame.pack(fill=X, pady=5)
        
        type_label = Label(type_frame, text="Type:")
        type_label.pack(side=LEFT)
        
        self.animal_type = StringVar(self.window)
        self.animal_type.set("Cat")  # Default value
        
        type_dropdown = OptionMenu(type_frame, self.animal_type, "Cat", "Dog", "Rabbit")
        type_dropdown.pack(side=RIGHT, expand=True, fill=X)
        
        # Add button
        self.add_button = Utils.button(main_frame, "Add", self.add_animal)
        self.add_button.pack(pady=10)
        self.add_button.config(state=DISABLED)
        
        # Cancel button
        cancel_button = Utils.button(main_frame, "Cancel", self.close)
        cancel_button.pack(pady=5)
        
        # Bind events to check fields
        self.name_entry.bind("<KeyRelease>", self.check_fields)
        self.age_entry.bind("<KeyRelease>", self.check_fields)
    
    def check_fields(self, event=None):
        if self.name_entry.get() and self.age_entry.get():
            self.add_button.config(state=NORMAL)
        else:
            self.add_button.config(state=DISABLED)
    
    def add_animal(self):
        name = self.name_entry.get()
        age_text = self.age_entry.get()
        animal_type = self.animal_type.get()
        
        # Validate that name doesn't already exist
        if self.animals.animal(name):
            error_msg = f"An animal with the name '{name}' already exists"
            ErrorView(error_msg, "InvalidOperationException")
            return
        
        # Validate that age is an integer
        try:
            age = int(age_text)
        except ValueError:
            error_msg = "Age must be an integer"
            ErrorView(error_msg, "InvalidOperationException")
            return
        
        # Create the animal based on type
        if animal_type == "Cat":
            new_animal = Cat(name, age)
        elif animal_type == "Dog":
            new_animal = Dog(name, age)
        else:  # Rabbit
            new_animal = Rabbit(name, age)
        
        # Add the animal to the adoption center
        self.animals.add(new_animal)
        
        # Call the callback to refresh the table
        self.callback()
        
        # Close the window
        self.close()
    
    def close(self):
        self.window.destroy()
