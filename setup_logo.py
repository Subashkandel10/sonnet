import os
import shutil
import tkinter as tk
from tkinter import filedialog

def setup_logo():
    # Create GUI root (we'll hide it)
    root = tk.Tk()
    root.withdraw()
    
    # Show file dialog to select the logo image
    file_path = filedialog.askopenfilename(
        title="Select the PROG2 logo image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
    )
    
    if not file_path:
        print("No file selected. Exiting.")
        return
    
    # Create the image directory if it doesn't exist
    if not os.path.exists('image'):
        os.makedirs('image')
    
    # Copy the selected file to the image directory with the name "prog2_logo.jpg"
    try:
        # Destination path
        dest_path = os.path.join('image', 'prog2_logo.jpg')
        
        # Copy the file
        shutil.copy2(file_path, dest_path)
        
        print(f"Logo image copied successfully to {dest_path}")
        print("The Manager Dashboard will now display your PROG2 logo.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("This script will help you set up the PROG2 logo image for the Manager Dashboard.")
    print("It will ask you to select the logo image file and copy it to the application.")
    input("Press Enter to continue...")
    
    setup_logo() 