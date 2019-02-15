#MUTT Parser GUI
from tkinter import Tk, Label, Button

from main import *

class ParserGUI:
    def __init__(self, master):
        self.master = master
        master.title("Helper")

        self.label = Label(master, text="Parser Helper")
        self.label.pack()

        self.greet_button = Button(master, text="Select file", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Execute", command=self.execute)
        self.close_button.pack()

        self.close_button = Button(master, text="Quit", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Select File")

    def execute(self):
        caller_helper({"c": True})

root = Tk()
my_gui = ParserGUI(root)
root.mainloop()