'''
************************************************************************************************************************
Author: Brandon Romero & Matthew Martinez
Assignment: Software Engineering Project (User Query Table)
Last Edited: 10/06/2022
Program Description: Produces a table with results of the specified query
************************************************************************************************************************
'''
import tkinter as tk        # Importing necessary modules
from tkinter import ttk     # Importing necessary modules

# Method to create a table that contains a list of users
def show_results():
    root = tk.Tk()
    root.geometry('1400x200')
    columns = ('ID', 'First_Name', 'Middle_Name', 'Last_Name', 'Phone', 'Email', 'Password', 'Admin', 'User_Since', 'Last_Login')
    tree = ttk.Treeview(root, columns=columns, show='headings')
    tree.heading('ID', text='ID')
    tree.heading('First_Name', text='First Name')
    tree.heading('Middle_Name', text='Middle Name')
    tree.heading('Last_Name', text='Last Name')
    tree.heading('Phone', text='Phone')
    tree.heading('Email', text='Email')
    tree.heading('Password', text='Password')
    tree.heading('Admin', text='Admin')
    tree.heading('User_Since', text='User Since')
    tree.heading('Last_Login', text='Last Login')

    tree.column('ID', width=75, anchor=tk.W)
    tree.column('First_Name', width=150, anchor=tk.W)
    tree.column('Middle_Name', width=150, anchor=tk.W)
    tree.column('Last_Name', width=150, anchor=tk.W)
    tree.column('Phone', width=150, anchor=tk.W)
    tree.column('Email', width=200, anchor=tk.CENTER)
    tree.column('Password', width=150, anchor=tk.W)
    tree.column('Admin', width=75, anchor=tk.W)
    tree.column('User_Since', width=150, anchor=tk.W)
    tree.column('Last_Login', width=150, anchor=tk.W)

    data = []
    for i in Results.userList:
        data.append((i.id, i.firstName, i.middleName, i.lastName, i.mobile, i.email, i.password, i.admin, i.userSince, i.lastLogin))
    for user in data:
        tree.insert('', tk.END, values=user)
    tree.grid(row=0, column=0, sticky='nsew')
    total_users = len(Results.userList).__str__()                # Total users found in query
    listed_users = len(data).__str__()
    root.title("Discovered Users ("+listed_users+" of "+total_users+" shown)")

    def clear_table():
        for row in tree.get_children():
            tree.delete(row)

    def fill_table():
        for order in data:  # Adding data to table
            tree.insert('', tk.END, values=order)
        data.clear()
        Results.userList.clear()
    clear_table()
    fill_table()
    root.mainloop()
# Class to create an object containing a list of users
class Results:
    userList = []
# Method to create and add a user to 'userList'
    def __init__(self, ID, First_Name, Middle_Name, Last_Name, Phone, Email, Password, Admin, User_Since, Last_Login):
        self.id = ID
        self.firstName = First_Name
        self.middleName = Middle_Name
        self.lastName = Last_Name
        self.mobile = Phone
        self.email = Email
        self.password = Password
        self.admin = Admin
        self.userSince = User_Since
        self.lastLogin = Last_Login
        Results.userList.append(self)
