'''
************************************************************************************************************************
Author: Brandon Romero & Matthew Martinez
Assignment: Software Engineering Project (Database Dashboard)
Last Edited: 10/06/2022
Program Description: Produces a graphical user interface with buttons made to access the various forms
************************************************************************************************************************
'''
from tkinter import *
import formNewUser              # Form to add NEW users to the database
import formCurrentUsers         # Form to query the CURRENT users in the database
import formServices             # Form to query the company's scheduled/available services
import formGenerateOrder        # Form to create a new purchase order for a customer
import formOrders               # Form to query the company's orders

# Functions used to open the various forms for add/viewing data within the database
def orders():
    search_orders = formOrders.orderInfo()
    search_orders()
def genOrder():
    createOrder = formGenerateOrder.generateOrder()
    createOrder()
def services():
    servicesView = formServices.viewServices()
    servicesView()
def currentUser():
    customerView = formCurrentUsers.currentAcc()
    customerView()
def newUser():
    customerAdd = formNewUser.newAcc()
    customerAdd()
# Creating the Database Dashboard, which is a GUI that allows program managers to access and manage the database
dbDash = Tk()
dbDash.title('Add New Customer')
dbDash.geometry('500x400')
dbDash.config(bg="light gray")
dbDash.attributes('-fullscreen',True)
# Frame, Labels, and Buttons
frame = Frame(dbDash, padx=20, pady=20)
frame.pack(expand=True)
Label(frame, text="Database Dashboard", font=("Times", "24", "bold")).grid(row=0, columnspan=7, pady=10)
reg = Button(frame, text="Register NEW Account", width=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=newUser)
chk = Button(frame, text="Search Customers", width=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=currentUser)
ordrs = Button(frame, text="Search Orders", width=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=orders)
srvcs = Button(frame, text="View Services", width=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=services)
faq = Button(frame, text="NEW Order", width=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=genOrder)
ext = Button(frame, text="Exit", width=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: dbDash.destroy())
reg.grid(row=6, column=1, pady=20)
chk.grid(row=6, column=3, pady=20)
ordrs.grid(row=6, column=5, pady=20)
srvcs.grid(row=7, column=1, pady=20)
faq.grid(row=7, column=3, pady=20)
ext.grid(row=7, column=5, pady=20)
dbDash.mainloop()
