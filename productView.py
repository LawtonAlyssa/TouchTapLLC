'''
************************************************************************************************************************
Author: Brandon Romero & Matthew Martinez
Assignment: Software Engineering Project (Product Query Table)
Last Edited: 10/06/2022
Program Description: Produces a table with results of the specified query
************************************************************************************************************************
'''
import tkinter as tk        # Importing necessary modules
from tkinter import ttk     # Importing necessary modules

# Method to create a table that contains a list of Products
def show_results():
    root = tk.Tk()
    root.geometry('1300x200')
    columns = ('prod_id', 'prod_title', 'meta_title', 'prod_slug', 'prod_summary', 'prod_type', 'prod_price',
               'prod_created', 'prod_content')
    tree = ttk.Treeview(root, columns=columns, show='headings')
    tree.heading('prod_id', text='Product ID')
    tree.heading('prod_title', text='Title')
    tree.heading('meta_title', text='Meta')
    tree.heading('prod_slug', text='Slug ID')
    tree.heading('prod_summary', text='Summary')
    tree.heading('prod_type', text='Type')
    tree.heading('prod_price', text='Price')
    tree.heading('prod_created', text='Created At')
    tree.heading('prod_content', text='Content')

    tree.column('prod_id', width=75, anchor=tk.W)
    tree.column('prod_title', width=200, anchor=tk.W)
    tree.column('meta_title', width=150, anchor=tk.W)
    tree.column('prod_slug', width=100, anchor=tk.W)
    tree.column('prod_summary', width=100, anchor=tk.CENTER)
    tree.column('prod_type', width=150, anchor=tk.W)
    tree.column('prod_price', width=100, anchor=tk.W)
    tree.column('prod_created', width=150, anchor=tk.W)
    tree.column('prod_content', width=300, anchor=tk.W)

    data = []
    for i in Results.productList:
        data.append((i.prodID, i.prodT, i.metaT, i.prodSLUG, i.prodSUM, i.prodTYPE, i.prodPRICE,
                     i.prodC, i.prodCON))
    for product in data:
        tree.insert('', tk.END, values=product)
    tree.grid(row=0, column=0, sticky='nsew')
    total_products = len(Results.productList).__str__()
    listed_products = len(data).__str__()
    root.title("Discovered Orders ("+listed_products+" of "+total_products+" shown)")

    def clear_table():
        for row in tree.get_children():
            tree.delete(row)

    def fill_table():
        for order in data:  # Adding data to table
            tree.insert('', tk.END, values=order)
        data.clear()
        Results.productList.clear()
    clear_table()
    fill_table()
    root.mainloop()
# Class to create an object containing a list of products/services
class Results:
    productList = []
    # Method to create and add a product to 'productList'
    def __init__(self, prod_id, prod_title, meta_title, prod_slug, prod_summary, prod_type, prod_price,
                 prod_created, prod_content):
        self.prodID = prod_id
        self.prodT = prod_title
        self.metaT = meta_title
        self.prodSLUG = prod_slug
        self.prodSUM = prod_summary
        self.prodTYPE = prod_type
        self.prodPRICE = prod_price
        self.prodC = prod_created
        self.prodCON = prod_content
        Results.productList.append(self)
