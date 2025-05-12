import os
import shutil
import tkinter as tk
from tkinter import filedialog

def copy_image():
    # Create GUI root (we'll hide it)
    root = tk.Tk()
    root.withdraw()
    
    # Show file dialog to select the image
    file_path = filedialog.askopenfilename(
        title="Select the error visualization image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
    )
    
    if not file_path:
        print("No file selected. Exiting.")
        return
    
    # Create the image directory if it doesn't exist
    if not os.path.exists('image'):
        os.makedirs('image')
    
    # Copy the selected file to the image directory with the name "error_code.jpg"
    try:
        # Destination path
        dest_path = os.path.join('image', 'error_code.jpg')
        
        # Copy the file
        shutil.copy2(file_path, dest_path)
        
        # Update the ErrorView.py file to use the new image
        with open('ErrorView.py', 'r') as file:
            content = file.read()
        
        # Replace the image path
        if 'error_banner.jpg' in content:
            content = content.replace('error_banner.jpg', 'error_code.jpg')
            
            # Write the updated content back to the file
            with open('ErrorView.py', 'w') as file:
                file.write(content)
            
            print(f"ErrorView.py has been updated to use the new image.")
        else:
            print("Note: Couldn't find 'error_banner.jpg' in ErrorView.py. You may need to manually update it.")
        
        print(f"Image copied successfully to {dest_path}")
        print("The error view will now display your image when errors occur.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("This script will help you set up your custom error visualization image.")
    print("It will ask you to select the image file and copy it to the application.")
    input("Press Enter to continue...")
    
    copy_image() 