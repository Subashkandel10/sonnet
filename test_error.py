from tkinter import *
from ErrorView import ErrorView
from model.exception.InvalidOperationException import InvalidOperationException

# This script demonstrates how the ErrorView displays errors with the image

def test_error():
    print("Testing the ErrorView with an error message...")
    root = Tk()
    root.withdraw()  # Hide the root window
    
    # Show an error with the InvalidOperationException
    ErrorView("This is a test error message to demonstrate the error view with the image.", 
              "InvalidOperationException")
    
    root.mainloop()

if __name__ == "__main__":
    test_error() 