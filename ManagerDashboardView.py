from tkinter import *
from tkinter import ttk
from Utils import Utils
from UserListView import UserListView
from AddAnimalView import AddAnimalView
from ErrorView import ErrorView
from model.exception.InvalidOperationException import InvalidOperationException
from model.Animal import Cat, Dog, Rabbit
from PIL import Image, ImageTk

class ManagerDashboardView:
    def __init__(self, manager, adoption_centre):
        self.manager = manager
        self.adoption_centre = adoption_centre
        self.current_filter = "all"
        
        self.root = Utils.root()
        self.root.title("Manager Dashboard")
        self.root.configure(bg="white")  # Changed to white background
        self.setup_ui()
        self.root.mainloop()
    
    def setup_ui(self):
        # Main frame with white background
        main_frame = Frame(self.root, bg="white")
        main_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        
        # Header with PROG2 logo
        header_frame = Frame(main_frame, bg="white")
        header_frame.pack(fill=X, pady=5)
        
        # Load and display the logo using cat_banner.jpg
        try:
            # Use cat_banner.jpg as the logo image
            logo_image = Image.open("image/cat_banner.jpg")
            logo_width = int(Utils.width // 1.5)  # Make it a bit wider and ensure integer
            logo_height = int(logo_width * 0.4)  # Adjust ratio as needed
            logo_image = logo_image.resize((logo_width, logo_height))
            logo_photo = ImageTk.PhotoImage(logo_image)
            
            logo_label = Label(header_frame, image=logo_photo, bg="white")
            logo_label.image = logo_photo  # Keep a reference
            logo_label.pack(pady=5)
            
          
            
           
        except Exception as e:
            print(f"Error loading image: {e}")
            # Fallback if image not found
            title_label = Label(header_frame, text="PROG2\nADOPTION CENTRE", font="Arial 16 bold", fg="#13937a", bg="white")
            title_label.pack(pady=10)
        
        # Manager Dashboard label (purple)
        dashboard_label = Label(main_frame, text="Manager Dashboard", font="Arial 12", fg="#8a7fff", bg="white")
        dashboard_label.pack(pady=10)
        
        # Filter buttons in a frame - keep the dark background for this section
        filter_frame = Frame(main_frame, bg="#202020")
        filter_frame.pack(fill=X, pady=5)
        
        # Each filter button with consistent styling - keeping this the same
        all_filter = Button(filter_frame, text="All", command=lambda: self.apply_filter("all"), 
                           bg="#333333", fg="white", relief=FLAT, width=10)
        all_filter.pack(side=LEFT, padx=2)
        
        cat_filter = Button(filter_frame, text="Cat", command=lambda: self.apply_filter("Cat"), 
                           bg="#333333", fg="white", relief=FLAT, width=10)
        cat_filter.pack(side=LEFT, padx=2)
        
        dog_filter = Button(filter_frame, text="Dog", command=lambda: self.apply_filter("Dog"), 
                            bg="#333333", fg="white", relief=FLAT, width=10)
        dog_filter.pack(side=LEFT, padx=2)
        
        rabbit_filter = Button(filter_frame, text="Rabbit", command=lambda: self.apply_filter("Rabbit"), 
                               bg="#333333", fg="white", relief=FLAT, width=10)
        rabbit_filter.pack(side=LEFT, padx=2)
        
        # Table view with styling - changed to white background
        columns = ("Name", "Type", "Age", "Adoption Status")
        
        # Frame to hold the treeview - now white
        tree_frame = Frame(main_frame, bg="white")
        tree_frame.pack(fill=BOTH, expand=True, pady=10)
        
        # Custom style for the treeview - change to white background
        style = ttk.Style()
        style.configure("Treeview", 
                        background="white", 
                        foreground="black",
                        fieldbackground="white",
                        borderwidth=0)
        style.configure("Treeview.Heading", 
                        background="#333333", 
                        foreground="#8a7fff",
                        relief=FLAT)
        style.map("Treeview", 
                  background=[('selected', '#e0e0ff')])  # Light purple selection
        
        # Create the treeview with styled headers
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", 
                                selectmode="browse", style="Treeview", height=12)
        self.tree.pack(fill=BOTH, expand=True)
        
        # Configure columns
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=CENTER, width=Utils.width//len(columns))
        
        # Configure column colors and formatting for white background
        self.tree.tag_configure('available', foreground='black')
        self.tree.tag_configure('adopted', foreground='#888888')  # Grey for adopted
        
        # Add scrollbar if needed
        scrollbar = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Populate the tree with initial data
        self.refresh_table()
        
        # Bottom button frame with white background
        button_frame = Frame(main_frame, bg="white")
        button_frame.pack(fill=X, pady=10)
        
        # Style the buttons - keep the purple
        add_btn = Button(button_frame, text="Add Animal", command=self.open_add_animal,
                        bg="#8a7fff", fg="white", relief=FLAT, width=15)
        add_btn.pack(side=LEFT, padx=5)
        
        self.remove_btn = Button(button_frame, text="Remove Animal", command=self.remove_animal,
                               bg="#8a7fff", fg="white", relief=FLAT, width=15)
        self.remove_btn.pack(side=LEFT, padx=5)
        self.remove_btn.config(state=DISABLED)
        
        user_list_btn = Button(button_frame, text="User List", command=self.open_user_list,
                              bg="#8a7fff", fg="white", relief=FLAT, width=15)
        user_list_btn.pack(side=LEFT, padx=5)
        
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
            adoption_status = "Adopted" if animal.is_already_adopted() else "Available"
            
            # Use different tag based on adoption status
            tag = 'adopted' if animal.is_already_adopted() else 'available'
            
            self.tree.insert("", END, values=(animal.get_name(), animal_type, animal.age, adoption_status), tags=(tag,))
    
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
