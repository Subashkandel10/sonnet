from tkinter import *
from Utils import Utils
from UserListView import UserListView
from AddAnimalView import AddAnimalView
from ErrorView import ErrorView
from model.exception.InvalidOperationException import InvalidOperationException
from model.Animal import Cat, Dog, Rabbit

class ManagerDashboardView:
    def __init__(self, manager, adoption_centre):
        self.manager = manager
        self.adoption_centre = adoption_centre
        self.current_filter = "all"
        
        self.root = Utils.root()
        self.root.title("Manager Dashboard")
        self.setup_ui()
        self.root.mainloop()
    
    def setup_ui(self):
        main_frame = Utils.frame(self.root)
        main_frame.pack(padx=20, pady=20)
        
        # Header with title
        header_frame = Utils.frame(main_frame)
        header_frame.pack(fill=X, pady=10)
        
        title_label = Utils.label(header_frame, "Manager Dashboard")
        title_label.pack(side=LEFT)
        
        # Buttons
        button_frame = Utils.frame(main_frame)
        button_frame.pack(fill=X, pady=10)
        
        add_btn = Utils.button(button_frame, "Add", self.open_add_animal)
        add_btn.pack(side=LEFT, padx=5)
        
        self.remove_btn = Utils.button(button_frame, "Remove", self.remove_animal)
        self.remove_btn.pack(side=LEFT, padx=5)
        self.remove_btn.config(state=DISABLED)
        
        user_list_btn = Utils.button(button_frame, "User List", self.open_user_list)
        user_list_btn.pack(side=LEFT, padx=5)
        
        # Filter buttons
        filter_frame = Utils.frame(main_frame)
        filter_frame.pack(fill=X, pady=10)
        
        all_filter = Utils.filter_button(filter_frame, "All", lambda: self.apply_filter("all"))
        all_filter.pack(side=LEFT, padx=5)
        
        cat_filter = Utils.filter_button(filter_frame, "Cat", lambda: self.apply_filter("Cat"))
        cat_filter.pack(side=LEFT, padx=5)
        
        dog_filter = Utils.filter_button(filter_frame, "Dog", lambda: self.apply_filter("Dog"))
        dog_filter.pack(side=LEFT, padx=5)
        
        rabbit_filter = Utils.filter_button(filter_frame, "Rabbit", lambda: self.apply_filter("Rabbit"))
        rabbit_filter.pack(side=LEFT, padx=5)
        
        # Table view
        columns = ("Name", "Type", "Age", "Adopted")
        self.tree = Utils.treeview(main_frame, columns)
        self.tree.pack(fill=BOTH, expand=True)
        
        # Populate tree with animals
        self.refresh_table()
        
        # Bind selection event
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
    
    def apply_filter(self, filter_type):
        self.current_filter = filter_type
        self.refresh_table()
        # Reset selection when filter is applied
        self.remove_btn.config(state=DISABLED)
    
    def refresh_table(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get animals based on current filter
        animals = self.adoption_centre.animals.get_animals_by_filter(self.current_filter)
        
        # Add animals to table
        for animal in animals:
            animal_type = type(animal).__name__
            adopted = "Yes" if animal.is_already_adopted() else "No"
            self.tree.insert("", END, values=(animal.get_name(), animal_type, animal.age, adopted))
    
    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            self.remove_btn.config(state=NORMAL)
        else:
            self.remove_btn.config(state=DISABLED)
    
    def open_user_list(self):
        UserListView(self.adoption_centre.get_users())
    
    def open_add_animal(self):
        AddAnimalView(self.adoption_centre.animals, self.refresh_table)
    
    def remove_animal(self):
        selected = self.tree.selection()
        if not selected:
            return
        
        values = self.tree.item(selected[0], 'values')
        animal_name = values[0]
        animal = self.adoption_centre.animals.animal(animal_name)
        
        if animal:
            try:
                if animal.is_already_adopted():
                    raise InvalidOperationException("Cannot remove an adopted animal")
                
                self.adoption_centre.animals.remove(animal)
                self.refresh_table()
                self.remove_btn.config(state=DISABLED)
            except InvalidOperationException as e:
                ErrorView(str(e), type(e).__name__)
