from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from db import Database
import tkinter as tk

db = Database('thriftstore.db')

LARGEFONT =("Verdana", 35)
app = Tk()
class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Thrift Store", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Add User",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Add Item",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Add User", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Home Page",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Add Item",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)
        # Buttons
        add_btn = Button(app, text='Add Item', width=12, command=add_item)
        add_btn.grid(row=2, column=0, pady=20)

        remove_btn = Button(app, text='Remove Item', width=12, command=remove_item)
        remove_btn.grid(row=2, column=1)

        update_btn = Button(app, text='Update Item', width=12, command=update_item)
        update_btn.grid(row=2, column=2)

        clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
        clear_btn.grid(row=2, column=3)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Add Item", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Add User",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Home Page",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()
# Info List Box
item_list = Listbox(app, height=8, width=50)
item_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# set scrollbar to listbox
item_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=item_list.yview)

# Bind select
# item_list.bind('<<ListboxSelect>>', select_item)

app.title('Thrift Store')
app.geometry('700x350')

#start program
app.mainloop()
