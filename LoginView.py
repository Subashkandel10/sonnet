from tkinter import *
from Utils import Utils
from model.AdoptionCentre import AdoptionCentre
from model.exception.UnauthorizedAccessException import UnauthorizedAccessException
from model.exception.InvalidOperationException import InvalidOperationException
from ErrorView import ErrorView
from CustomerDashboardView import CustomerDashboardView
from ManagerDashboardView import ManagerDashboardView

class LoginView:
    def __init__(self):
        self.root = Utils.root()
        self.adoption_centre = AdoptionCentre()
        self.setup_ui()
        self.root.mainloop()
        
    def setup_ui(self):
        # Create title and main frame
        self.main_frame = Utils.frame(self.root)
        self.main_frame.pack(padx=20, pady=20)
        
        # Add image
        img = Utils.image(self.main_frame, "image/cat_banner.jpg")  # Using available image
        img.pack()
        
        # Customer login section
        self.customer_frame = Utils.frame(self.main_frame)
        self.customer_frame.pack(fill=X, pady=10)
        
        customer_label = Utils.label(self.customer_frame, "Customer Login")
        customer_label.pack(anchor=W)
        
        # Username field
        username_frame = Frame(self.customer_frame)
        username_frame.pack(fill=X, pady=5)
        
        username_label = Label(username_frame, text="Username:")
        username_label.pack(side=LEFT)
        
        self.username_entry = Entry(username_frame)
        self.username_entry.pack(side=RIGHT, expand=True, fill=X)
        
        # Email field
        email_frame = Frame(self.customer_frame)
        email_frame.pack(fill=X, pady=5)
        
        email_label = Label(email_frame, text="Email:")
        email_label.pack(side=LEFT)
        
        self.email_entry = Entry(email_frame)
        self.email_entry.pack(side=RIGHT, expand=True, fill=X)
        
        # Separator
        separator = Utils.separator(self.main_frame)
        separator.pack(fill=X, pady=10)
        
        # Manager login section
        self.manager_frame = Utils.frame(self.main_frame)
        self.manager_frame.pack(fill=X, pady=10)
        
        manager_label = Utils.label(self.manager_frame, "Manager Login")
        manager_label.pack(anchor=W)
        
        # Manager ID field
        manager_id_frame = Frame(self.manager_frame)
        manager_id_frame.pack(fill=X, pady=5)
        
        manager_id_label = Label(manager_id_frame, text="Manager ID:")
        manager_id_label.pack(side=LEFT)
        
        self.manager_id_entry = Entry(manager_id_frame)
        self.manager_id_entry.pack(side=RIGHT, expand=True, fill=X)
        
        # Login button
        self.login_button = Utils.button(self.main_frame, "Login", self.login)
        self.login_button.pack(pady=10)
        self.login_button.config(state=DISABLED)
        
        # Bind events for advanced functionality
        self.username_entry.bind("<KeyRelease>", self.check_login_fields)
        self.email_entry.bind("<KeyRelease>", self.check_login_fields)
        self.manager_id_entry.bind("<KeyRelease>", self.check_login_fields)
    
    def check_login_fields(self, event=None):
        # Handle disabling/enabling fields based on content
        if self.manager_id_entry.get():
            self.username_entry.config(state=DISABLED)
            self.email_entry.config(state=DISABLED)
            self.login_button.config(state=NORMAL)
        elif self.username_entry.get() or self.email_entry.get():
            self.manager_id_entry.config(state=DISABLED)
            # Enable login button only if both username and email have content
            if self.username_entry.get() and self.email_entry.get():
                self.login_button.config(state=NORMAL)
            else:
                self.login_button.config(state=DISABLED)
        else:
            # Reset all fields to enabled if nothing is entered
            self.username_entry.config(state=NORMAL)
            self.email_entry.config(state=NORMAL)
            self.manager_id_entry.config(state=NORMAL)
            self.login_button.config(state=DISABLED)
    
    def login(self):
        try:
            if self.manager_id_entry.get():
                # Manager login
                manager = self.adoption_centre.get_users().validate_manager(self.manager_id_entry.get())
                if manager:
                    self.root.destroy()
                    ManagerDashboardView(manager, self.adoption_centre)
            else:
                # Customer login
                customer = self.adoption_centre.get_users().validate_customer(
                    self.username_entry.get(), self.email_entry.get())
                if customer:
                    self.root.destroy()
                    CustomerDashboardView(customer, self.adoption_centre)
                else:
                    raise UnauthorizedAccessException("Invalid customer credentials")
        except (InvalidOperationException, UnauthorizedAccessException) as e:
            ErrorView(str(e), type(e).__name__)

if __name__ == "__main__":
    LoginView()
