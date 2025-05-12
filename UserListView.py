from tkinter import *
from Utils import Utils

class UserListView:
    def __init__(self, users):
        self.users = users
        self.window = Utils.top_level("User List")
        self.setup_ui()
        self.window.grab_set()  # Make window modal
    
    def setup_ui(self):
        main_frame = Utils.frame(self.window)
        main_frame.pack(padx=20, pady=20)
        
        # Title
        title_label = Utils.label(main_frame, "User List")
        title_label.pack(pady=10)
        
        # User list view
        columns = ["Users"]
        self.tree = Utils.treeview(main_frame, columns)
        self.tree.pack(fill=BOTH, expand=True)
        
        # Populate with users
        for user in self.users.get_users():
            self.tree.insert("", END, values=(str(user),))
        
        # Close button
        close_button = Utils.button(main_frame, "Close", self.close)
        close_button.pack(pady=10)
    
    def close(self):
        self.window.destroy()
