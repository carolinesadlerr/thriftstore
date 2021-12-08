from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from db import Database

# Initialize Database
db = Database('thriftstore.db')


# Function to fill item list
def populate_list():
    item_list.delete(0, END)
    for row in db.fetch():
        item_list.insert(END, row)


# Function to add items
# verifies that all fields are filled before adding
def add_item():
    if item_text.get() == '' or des_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(item_text.get(), des_text.get(), price_text.get())
    item_list.delete(0, END)
    item_list.insert(END, (item_text.get(), des_text.get(), price_text.get()))
    populate_list()


# Function to create an event that when you select item
# it takes the index so it can be deleted or updated
def select_item(event):
    try:
        global selected_item
        index = item_list.curselection()[0]
        selected_item = item_list.get(index)

        item_entry.delete(0, END)
        item_entry.insert(END, selected_item[1])
        des_entry.delete(0, END)
        des_entry.insert(END, selected_item[2])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[3])
    except IndexError:
        pass


# Function to remove item selected by user
def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


# Function to update an item
def update_item():
    db.update(selected_item[0], item_text.get(), des_text.get(), price_text.get())
    populate_list()


# function to clear the text inside the text fields
def clear_text():
    item_entry.delete(0, END)
    des_entry.delete(0, END)
    price_entry.delete(0, END)


# create window
app = Tk()

# Item
item_text = StringVar()
item_label = Label(app, text='Item', font=('bold', 14), pady=20)
item_label.grid(row=0, column=0)
item_entry = Entry(app, textvariable=item_text)
item_entry.grid(row=0, column=1)

# Description
des_text = StringVar()
des_label = Label(app, text='Description', font=('bold', 14))
des_label.grid(row=0, column=2)
des_entry = Entry(app, textvariable=des_text)
des_entry.grid(row=0, column=3)

# Price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14))
price_label.grid(row=1, column=0)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=1)

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
item_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Item', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Item', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Item', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

# Changes the Title of the application
app.title('Thrift Store')

# sets size of application box
app.geometry('700x350')

# populate data
populate_list()
# start program
app.mainloop()
