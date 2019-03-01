#MUTT Parser GUI
from tkinter import Tk, Label, Button, IntVar, Checkbutton

from main import *

class ParserGUI:
    def __init__(self, master):
        self.init_args()
        self.master = master
        master.title("Helper")

        self.label = Label(master, text="Parser Helper")
        self.label.pack()

        self.exception_value = IntVar()
        # Exception
        C1 = Checkbutton(master, text="Exception", variable=self.exception_value, \
                         onvalue=1, offvalue=0, height=5, \
                         width=20)
        C1.pack()


        self.cause_value = IntVar()
        # Cause by
        C2 = Checkbutton(master, text="Cause by", variable=self.cause_value, \
                         onvalue=1, offvalue=0, height=5, \
                         width=20)
        C2.pack()
        # Verbose
        self.verbose_value = IntVar()
        C3 = Checkbutton(master, text="Verbose", variable=self.verbose_value, \
                         onvalue=1, offvalue=0, height=5, \
                         width=20)
        C3.pack()

        # Log to file
        self.log_value = IntVar()
        C4 = Checkbutton(master, text="Log to file", variable=self.log_value, \
                         onvalue=1, offvalue=0, height=5, \
                         width=20)
        C4.pack()

        self.greet_button = Button(master, text="Select file", command=self.open_file)
        self.greet_button.pack()

        self.close_button = Button(master, text="Execute", command=self.execute)
        self.close_button.pack()

        self.close_button = Button(master, text="Quit", command=master.quit)
        self.close_button.pack()

    def init_args(self):
        self.args_dict ={}
        self.args_dict["file"] = "server.log"
        self.args_dict["exception"] = False
        self.args_dict["verbose"] = False
        self.args_dict["unique"] = False
        self.args_dict["xerror"] = False
        self.args_dict["cause"] = False
        self.args_dict["snraw"] = False
        self.args_dict["kcs"] = False
        self.args_dict["google"] = False
        self.args_dict["write"] = False
        self.args_dict["log"] = False

    def open_file(self):
        from tkinter.filedialog import askopenfilename
        file_address = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        print(file_address)
        self.args_dict["file"] = file_address
        #caller_helper(args_dict=self.args_dict)

    def execute(self):
        self.args_dict["exception"] = bool(self.exception_value.get())
        self.args_dict["cause"] = bool(self.cause_value.get())
        self.args_dict["verbose"] = bool(self.verbose_value.get())
        caller_helper(args_dict=self.args_dict)

root = Tk()
my_gui = ParserGUI(root)
root.mainloop()