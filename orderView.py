'''
************************************************************************************************************************
Author: Brandon Romero & Matthew Martinez
Assignment: Software Engineering Project (Order Query Table)
Last Edited: 10/06/2022
Program Description: Produces a table with results of the specified query
************************************************************************************************************************
'''
import tkinter as tk
from tkinter import ttk

# Method to create a table that contains a list of Orders
def show_results():
    root = tk.Tk()
    root.geometry('1200x200')
    columns = (
    'order_ID', 'user_ID', 'order_status', 'sub_total', 'taxes', 'Shipping', 'order_total', 'order_grand_total',
    'date_created', 'order_content', 'prod_ID', 'token_ID')
    tree = ttk.Treeview(root, columns=columns, show='headings')
    tree.heading('order_ID', text='Order ID')
    tree.heading('user_ID', text='User ID')
    tree.heading('order_status', text='Order Status')
    tree.heading('sub_total', text='Sub Total')
    tree.heading('taxes', text='Tax')
    tree.heading('Shipping', text='Shipping')
    tree.heading('order_total', text='Total')
    tree.heading('order_grand_total', text='Grand Total')
    tree.heading('date_created', text='Date Created')
    tree.heading('order_content', text='Contents')
    tree.heading('prod_ID', text='Product ID')
    tree.heading('token_ID', text='Token ID')

    tree.column('order_ID', width=75, anchor=tk.W)
    tree.column('user_ID', width=75, anchor=tk.W)
    tree.column('order_status', width=75, anchor=tk.W)
    tree.column('sub_total', width=100, anchor=tk.CENTER)
    tree.column('taxes', width=100, anchor=tk.W)
    tree.column('Shipping', width=100, anchor=tk.W)
    tree.column('order_total', width=100, anchor=tk.W)
    tree.column('order_grand_total', width=100, anchor=tk.W)
    tree.column('date_created', width=150, anchor=tk.W)
    tree.column('order_content', width=150, anchor=tk.W)
    tree.column('prod_ID', width=75, anchor=tk.W)
    tree.column('token_ID', width=75, anchor=tk.W)
    data = []
    for i in Results.orderList:
        data.append((i.id, i.userID, i.orderStatus, i.subTotal, i.taxes, i.shipping, i.ordTotal,
                     i.ordGrandTotal, i.dateCreated, i.ordContent, i.prodID,  i.tokenID))  # Adding orders to new array
    tree.grid(row=0, column=0, sticky='nsew')
    total_orders = len(Results.orderList).__str__()  # Total orders found in search
    listed_orders = len(data).__str__()
    root.title("Discovered Orders (" + listed_orders + " of " + total_orders + " shown)")

    def clear_table():
        for row in tree.get_children():
            tree.delete(row)

    def fill_table():
        for order in data:  # Adding data to table
            tree.insert('', tk.END, values=order)
        data.clear()
        Results.orderList.clear()
    clear_table()
    fill_table()
    root.mainloop()
# Class to create an object containing a list of orders
class Results:
    orderList = []
    # Method to create and add an order to 'orderList'
    def __init__(self, order_ID, user_ID, order_status, sub_total, taxes, Shipping, order_total, order_grand_total, date_created, order_content, prod_ID, token_ID):
        self.id = order_ID
        self.userID = user_ID
        self.orderStatus = order_status
        self.subTotal = sub_total
        self.taxes = taxes
        self.shipping = Shipping
        self.ordTotal = order_total
        self.ordGrandTotal = order_grand_total
        self.dateCreated = date_created
        self.ordContent = order_content
        self.prodID = prod_ID
        self.tokenID = token_ID
        Results.orderList.append(self)
