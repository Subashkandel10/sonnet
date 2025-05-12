from tkinter import *
from Utils import Utils

class ErrorView:
    def __init__(self, message, exception_type):
        self.window = Utils.top_level("Error")
        self.setup_ui(message, exception_type)
        self.window.grab_set()  # Make window modal
        
    def setup_ui(self, message, exception_type):
        main_frame = Utils.frame(self.window)
        main_frame.pack(padx=20, pady=20)
        
        # Add error image 
        error_img = Utils.image(main_frame, "image/error_banner.jpg")
        error_img.pack(pady=10)
        
        # Exception type label
        exception_label = Utils.label(main_frame, exception_type)
        exception_label.pack(pady=10)
        
        # Error message
        message_label = Label(main_frame, text=message, wraplength=400)
        message_label.pack(pady=10)
        
        # OK button
        ok_button = Utils.button(main_frame, "OK", self.close)
        ok_button.pack(pady=10)
        
    def close(self):
        self.window.destroy()
