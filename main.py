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


# Function to fill user list
def populate_userlist():
    user_list.delete(0, END)
    for rows2 in db.fetch2():
        user_list.insert(END, rows2)


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


def add_user():
    if user_text.get() == '' or email_text.get() == '' or number_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert_user(user_text.get(), email_text.get(), number_text.get())
    user_list.delete(0, END)
    user_list.insert(END, (user_text.get(), email_text.get(), number_text.get()))
    populate_userlist()


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


def select_user(event):
    try:
        global selected_user
        index = user_list.curselection()[0]
        selected_user = user_list.get(index)

        user_entry.delete(0, END)
        user_entry.insert(END, selected_user[1])
        email_entry.delete(0, END)
        email_entry.insert(END, selected_user[2])
        number_entry.delete(0, END)
        number_entry.insert(END, selected_user[3])
    except IndexError:
        pass


# Function to remove item selected by user
def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def remove_user():
    db.remove_user(selected_user[0])
    clear_text()
    populate_userlist()


# Function to update an item
def update_item():
    db.update(selected_item[0], item_text.get(), des_text.get(), price_text.get())
    populate_list()


def update_user():
    db.update_user(selected_user[0], user_text.get(), email_text.get(), number_text.get())
    populate_userlist()


# function to clear the text inside the text fields
def clear_text():
    item_entry.delete(0, END)
    des_entry.delete(0, END)
    price_entry.delete(0, END)
    user_entry.delete(0, END)
    email_entry.delete(0, END)
    number_entry.delete(0, END)


# create window
app = Tk()

# Item
item_text = StringVar()
item_label = Label(app, text='Item', font=('bold', 10), pady=10)
item_label.grid(row=0, column=0)
item_entry = Entry(app, textvariable=item_text)
item_entry.grid(row=0, column=1)

# Description
des_text = StringVar()
des_label = Label(app, text='Description', font=('bold', 10))
des_label.grid(row=1, column=0)
des_entry = Entry(app, textvariable=des_text)
des_entry.grid(row=1, column=1)

# Price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 10))
price_label.grid(row=2, column=0)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=2, column=1)

# User
user_text = StringVar()
user_label = Label(app, text='User', font=('bold', 10))
user_label.grid(row=0, column=2)
user_entry = Entry(app, textvariable=user_text)
user_entry.grid(row=0, column=3)
# email
email_text = StringVar()
email_label = Label(app, text='Email', font=('bold', 10))
email_label.grid(row=1, column=2)
email_entry = Entry(app, textvariable=email_text)
email_entry.grid(row=1, column=3)
# phone number
number_text = StringVar()
number_label = Label(app, text='Phone number', font=('bold', 10))
number_label.grid(row=2, column=2)
number_entry = Entry(app, textvariable=number_text)
number_entry.grid(row=2, column=3)

# Info List Box
item_list = Listbox(app, height=8, width=50)
item_list.grid(row=5, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# User List Box
user_list = Listbox(app, height=8, width=50)
user_list.grid(row=5, column=3, columnspan=3, rowspan=6, pady=20, padx=20)

# create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=5, column=2)

# set scrollbar to listbox
item_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=item_list.yview)

# Bind select
item_list.bind('<<ListboxSelect>>', select_item)
# Bind select
user_list.bind('<<ListboxSelect>>', select_user)

# Buttons
add_btn = Button(app, text='Add Item', width=12, command=add_item)
add_btn.grid(row=4, column=0, pady=10)

remove_btn = Button(app, text='Remove Item', width=12, command=remove_item)
remove_btn.grid(row=4, column=1)

update_btn = Button(app, text='Update Item', width=12, command=update_item)
update_btn.grid(row=4, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=4, column=3)

# Buttons
addUser_btn = Button(app, text='Add User', width=12, command=add_user)
addUser_btn.grid(row=4, column=4, pady=10)

removeUser_btn = Button(app, text='Remove user', width=12, command=remove_user)
removeUser_btn.grid(row=4, column=5)

updateUser_btn = Button(app, text='Update User', width=12, command=update_user)
updateUser_btn.grid(row=4, column=6)

# Changes the Title of the application
app.title('Thrift Store')

# sets size of application box
app.geometry('900x350')

# populate data
populate_list()
populate_userlist()
# start program
app.mainloop()
