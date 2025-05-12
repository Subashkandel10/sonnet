from tkinter import *
from Utils import Utils
from DetailsView import DetailsView
from ErrorView import ErrorView
from model.exception.InvalidOperationException import InvalidOperationException

class CustomerDashboardView:
    def __init__(self, customer, adoption_centre):
        self.customer = customer
        self.adoption_centre = adoption_centre
        
        self.root = Utils.root()
        self.root.title("Customer Dashboard")
        self.setup_ui()
        self.root.mainloop()
    
    def setup_ui(self):
        main_frame = Utils.frame(self.root)
        main_frame.pack(padx=20, pady=20)
        
        # Welcome message
        welcome_label = Utils.label(main_frame, f"Welcome, {self.customer.get_first_name()}")
        welcome_label.pack(anchor=W, pady=10)
        
        # Buttons
        button_frame = Utils.frame(main_frame)
        button_frame.pack(fill=X, pady=10)
        
        self.adopt_btn = Utils.button(button_frame, "Adopt", self.adopt_animal)
        self.adopt_btn.pack(side=LEFT, padx=5)
        self.adopt_btn.config(state=DISABLED)
        
        details_btn = Utils.button(button_frame, "My Details", self.open_details)
        details_btn.pack(side=LEFT, padx=5)
        
        # Table view of adoptable animals
        columns = ("Name", "Type", "Age")
        self.tree = Utils.treeview(main_frame, columns)
        self.tree.pack(fill=BOTH, expand=True)
        
        # Populate tree with adoptable animals
        self.refresh_table()
        
        # Bind selection event
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
    
    def refresh_table(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get adoptable animals only
        animals = self.adoption_centre.get_adoptable_animals()
        
        # Add animals to table
        for animal in animals:
            animal_type = type(animal).__name__
            self.tree.insert("", END, values=(animal.get_name(), animal_type, animal.age))
    
    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            self.adopt_btn.config(state=NORMAL)
        else:
            self.adopt_btn.config(state=DISABLED)
    
    def open_details(self):
        DetailsView(self.customer)
    
    def adopt_animal(self):
        selected = self.tree.selection()
        if not selected:
            return
        
        values = self.tree.item(selected[0], 'values')
        animal_name = values[0]
        
        # Find the animal object
        for animal in self.adoption_centre.get_adoptable_animals():
            if animal.get_name() == animal_name:
                try:
                    # Check if customer can adopt this type of animal
                    if not self.customer.can_adopt(animal):
                        animal_type = type(animal).__name__
                        raise InvalidOperationException(f"You cannot adopt more than {self.customer.ADOPTION_LIMIT} {animal_type}s")
                    
                    # Add to customer's adopted animals
                    self.customer.get_adopted_animals().add(animal)
                    
                    # Mark as adopted
                    animal.adopt()
                    
                    # Refresh table
                    self.refresh_table()
                    self.adopt_btn.config(state=DISABLED)
                    
                except InvalidOperationException as e:
                    ErrorView(str(e), type(e).__name__)
                break
