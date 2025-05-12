from tkinter import *
from Utils import Utils

class DetailsView:
    def __init__(self, customer):
        self.customer = customer
        self.window = Utils.top_level("My Details")
        self.setup_ui()
        self.window.grab_set()  # Make window modal
    
    def setup_ui(self):
        main_frame = Utils.frame(self.window)
        main_frame.pack(padx=20, pady=20)
        
        # Customer name
        name_label = Utils.label(main_frame, self.customer.get_name())
        name_label.pack(pady=10)
        
        # Title for adopted animals
        adopted_label = Utils.label(main_frame, "Adopted Animals")
        adopted_label.pack(pady=10)
        
        # Adopted animals list
        columns = ["Adopted Animals"]
        self.tree = Utils.treeview(main_frame, columns)
        self.tree.pack(fill=BOTH, expand=True)
        
        # Populate with adopted animals
        adopted_animals = self.customer.get_adopted_animals().get_animals()
        
        if adopted_animals:
            for animal in adopted_animals:
                self.tree.insert("", END, values=(str(animal),))
        
        # Close button
        close_button = Utils.button(main_frame, "Close", self.close)
        close_button.pack(pady=10)
    
    def close(self):
        self.window.destroy()
