from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

#You will never have to manually call this
class ObservableButton(Button):
    def __init__(self, root, text, callback, main_color, hover_color):
        Button.__init__(self, root, text=text, command=callback, background=main_color, padx=0, relief=FLAT,
                   font="Arial 11 bold", foreground="white")
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_exit)
        self.main_color = main_color
        self.hover_color = hover_color

    def on_hover(self, event):
        self["background"] = self.hover_color

    def on_exit(self, event):
        self["background"] = self.main_color

class Utils:
    purple = "#be8fff"
    width = 550
    image_height = 250

    @staticmethod
    def disable():
        pass

    @staticmethod
    def root():
        window = Tk()
        window.resizable(False, False)
        window.title("Login")
        return window


    #Some operating systems struggle to automatically stretch the window
    #If needed, pass in a manual height and uncomment line 46
    @staticmethod
    def top_level(title_, height=0):
        tl = Toplevel()
        tl.resizable(False, False)
        tl.title(title_)
        # tl.geometry(f"{Utils.width}x{height}")
        return tl

    @staticmethod
    def button(root, text_, callback=None):
        return ObservableButton(root, text_, callback, Utils.purple, "#aa82ff")

    @staticmethod
    def filter_button(root, text_, callback=None):
        return ObservableButton(root, text_, callback, "#444444", "#333333")

    @staticmethod
    def frame(root):
        return Frame(root, width=Utils.width)

    @staticmethod
    def separator(root):
        return ttk.Separator(root, orient='horizontal')

    @staticmethod
    def label(root, text_):
        return Label(root, text=text_, font="Helvetica 12 bold", foreground=Utils.purple)

    @staticmethod
    def image(root, path):
        image_ = ImageTk.PhotoImage(Image.open(path).resize((Utils.width, Utils.image_height)))
        lbl = Label(root, image=image_)
        lbl.photo = image_
        return lbl

    @staticmethod
    def treeview(root, columns, multi=False):
        tree = ttk.Treeview(root, show="headings", height=12, columns=columns, selectmode="extended" if multi else "browse")
        for column in tree["columns"]:
            tree.column(column, anchor=CENTER, width=int(Utils.width/len(columns)), stretch=NO)
        for i in range(len(columns)):
            tree.heading(i, text=columns[i])
        tree.bind("<Motion>", 'break')
        return tree
