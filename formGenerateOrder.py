'''
************************************************************************************************************************
Author: Brandon Romero & Matthew Martinez
Assignment: Software Engineering Project (FORM for the program's FAQ's and help resources)
Last Edited: 10/06/2022
Program Description: A GUI window for viewing tips on how to utilize the system
 * Input: Selection based query where buttons are pressed to perform a query
 * Output: A list containing the results of the query
************************************************************************************************************************
'''
from tkinter import *
from tkinter import messagebox
import smtplib
import ssl
import pymysql
import datetime

class generateOrder:
    def __call__(self):
        self.ws = Tk()
        self.ws.title('Create New Order')
        self.ws.geometry('500x400')
        self.ws.config(bg="light gray")
        self.ws.attributes('-fullscreen', True)

        # Frame and Labels
        frame = Frame(self.ws, padx=20, pady=20)
        frame.pack(expand=True)
        Label(frame, text="New Order", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        Label(frame, text='User ID', font=("Times", "14")).grid(row=1, column=0, pady=5)
        Label(frame, text='Product ID', font=("Times", "14")).grid(row=2, column=0, pady=5)
        Label(frame, text='Sub-Total', font=("Times", "14")).grid(row=3, column=0, pady=5)
        Label(frame, text='Shipping', font=("Times", "14")).grid(row=4, column=0, pady=5)
        Label(frame, text='Discounts', font=("Times", "14")).grid(row=5, column=0, pady=1)
        Label(frame, text='Purchase Token', font=("Times", "14")).grid(row=6, column=0, pady=5)
        Label(frame, text='Taxes', font=("Times", "14")).grid(row=8, column=0, pady=5)
        Label(frame, text='Grand-Total', font=("Times", "14")).grid(row=9, column=0, pady=5)



        # Entry Boxes
        self.userId = Entry(frame, width=30)
        self.prodId = Entry(frame, width=30)
        self.subT = Entry(frame, width=30)
        self.ship = Entry(frame, width=30)
        self.discount = Entry(frame, width=30)
        self.token = Entry(frame, width=30)
        self.tax = Entry(frame, width=30)
        self.grandT = Entry(frame, width=30)


        self.userId.grid(row=1, column=1)
        self.prodId.grid(row=2, column=1)
        self.subT.grid(row=3, column=1)
        self.ship.grid(row=4, column=1)
        self.discount.grid(row=5, column=1)
        self.token.grid(row=6, column=1)
        self.tax.grid(row=8, column=1)
        self.grandT.grid(row=9, column=1)
        self.tax.insert(0, 'Click Calculate')
        self.grandT.insert(0, 'Click Calculate')


        # Buttons
        clr = Button(frame, text="Clear", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),
                     command=self.clear)
        reg = Button(frame, text="Submit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),
                     command=self.submit)
        cal = Button(frame, text="Calculate", padx=10, relief=SOLID, font=("Times", "12", "bold"),
                     command=self.sum)
        ext = Button(frame, text="Back", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),
                     command=lambda: self.ws.destroy())

        clr.grid(row=11, column=0, pady=20)
        reg.grid(row=11, column=1, pady=20)
        cal.grid(row=10, column=1)
        ext.grid(row=11, column=2, pady=20)

        self.ws.mainloop()

    def sum(self):
        self.tax.delete(0, END)
        self.grandT.delete(0, END)
        subtot = int(self.subT.get())
        shipcost = int(self.ship.get())
        disco = int(self.discount.get())
        check_term = self.prodId.get()
        host = "127.0.0.1"
        port = int(3306)
        user = "root"
        password = "1qaz1qaz!QAZ!QAZ"
        dbname = "shop"
        mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
        cursor = mydb.cursor()
        check_for = "id"
        searchProd = "SELECT * FROM shop.product WHERE " + check_for + " = %s"
        cursor.execute(searchProd, check_term)
        result = cursor.fetchone()
        total = result[6]
        taxcost = (subtot + shipcost + total - disco) * 0.08
        gtot = subtot + shipcost + total + taxcost - disco
        self.tax.insert(0, taxcost)
        self.grandT.insert(0, gtot)

    def submit(self):
        userid_check = self.userId.get()
        prodid_check = self.prodId.get()
        subT_check = self.subT.get()
        tax_check = self.tax.get()
        ship_check = self.ship.get()
        discount_check = self.discount.get()
        token_check = self.token.get()

        current_time = datetime.datetime.now()
        yyyy = str(current_time.year)
        mm = str(current_time.month)
        dd = str(current_time.day)
        hh = str(current_time.hour)
        m_m = str(current_time.minute)
        ss = str(current_time.second)

        date_time = yyyy + '-' + mm + '-' + dd + ' ' + hh + ':' + m_m + ':' + ss
        check_count = 0
        if userid_check == "":
            warn = "User ID is Blank!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if prodid_check == "":
            warn = "Product ID can't be empty!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if subT_check == "":
            warn = "Sub-Total can't be empty!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if tax_check == "":
            warn = "Taxes can't be empty!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if ship_check == "":
            warn = "Shipping Costs can't be empty!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if discount_check == "":
            warn = "Discount can't be empty!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if token_check == "":
            warn = "Purchase Token can't be empty!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if check_count == 7:
            host = "127.0.0.1"
            port = int(3306)
            user = "root"
            password = "1qaz1qaz!QAZ!QAZ"
            dbname = "shop"
            mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
            cursor = mydb.cursor()
            userID = self.userId.get()
            productID = self.prodId.get()
            subTotal = self.subT.get()
            shipping = self.ship.get()
            discount = self.discount.get()
            token = self.token.get()
            check_term = productID
            check_for = "id"
            searchProd = "SELECT * FROM shop.product WHERE "+check_for+" = %s"
            cursor.execute(searchProd, check_term)
            result = cursor.fetchone()
            discount = int(discount)
            shipping = int(shipping)
            subTotal = int(subTotal)
            total = result[6]
            taxes = (subTotal + shipping + total - discount) * 0.08
            grandTotal = total + subTotal + shipping + taxes - discount
            content = result[8]
            new_order = ('0', userID, '1', subTotal, taxes, shipping, total, grandTotal, date_time, content, productID, token)
            cursor.execute('INSERT INTO shop.order VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                           (new_order[0], new_order[1], new_order[2], new_order[3], new_order[4], new_order[5],
                            new_order[6], new_order[7], new_order[8], new_order[9], new_order[10], new_order[11]))
            mydb.commit()

            # Searching database for user's email address
            check_user = userID
            check_id = "id"
            searchUser = "SELECT * FROM shop.user WHERE "+check_id+" = %s"
            cursor.execute(searchUser, check_user)
            user = cursor.fetchone()
            email = str(user[5])

            # Sending email to customer, which contains the unique purchase token to continue with the order
            port = int(587)  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = "simpliegreen@gmail.com"
            receiver_email = email
            password = "pzuuozowpitgvjad"
            FROM = 'Touch Tap LLC'
            SUBJECT = 'Order Token'
            TEXT = 'Input the following order token to confirm your purchase: ' + token
            message = """\
            From: %s
            %s
            %s
            """ % (FROM, SUBJECT, TEXT)
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls(context=context)
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            self.ws.destroy()
        else:
            warn = "An unknown error occurred!"
            messagebox.showerror('', warn)

    def clear(self):
        self.tax.delete(0, END)
        self.grandT.delete(0, END)
        self.tax.insert(0, 'Click Calculate')
        self.grandT.insert(0, 'Click Calculate')
        self.userId.delete(0, END)
        self.prodId.delete(0, END)
        self.subT.delete(0, END)
        self.ship.delete(0, END)
        self.discount.delete(0, END)
        self.token.delete(0, END)
