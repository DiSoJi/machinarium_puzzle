from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from find_sol import *

class states():
    def __init__(self):
        self.root = Toplevel()
        self.root.title('State Diagram')
        self.root.geometry('792x695')
        self.root.resizable(1,1)

        background_image=PhotoImage(file="state_diagram.png")
        background_label = Label(self.root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.root.mainloop()

def open_app():
    states_app = states()
    return 0

if __name__ == '__main__':
    open_app()
