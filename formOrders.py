'''
************************************************************************************************************************
Author: Brandon Romero & Matthew Martinez
Assignment: Software Engineering Project (FORM for viewing orders)
Last Edited: 10/06/2022
Program Description: A GUI window to perform a search of all orders stored within the database
 * Input: Selection of query type based on button presses. Search performed using string input provided by user
 * Output: A list containing the results of the query
************************************************************************************************************************
'''
from tkinter import *
from tkinter import messagebox
import pymysql
import orderView

class orderInfo:
    def __init__(self):
        self.lname = None
        self.orderNum = None
        self.openOrder = None
        self.completeOrder = None

    def __call__(self):
        self.ws = Tk()
        self.ws.title('Search Orders')
        self.ws.geometry('500x400')
        self.ws.config(bg="light gray")
        self.ws.attributes('-fullscreen', True)
        # Frame and Labels
        frame = Frame(self.ws, padx=20, pady=20)
        frame.pack(expand=True)
        Label(frame, text="Search Orders", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        # Buttons
        nameButton = Button(frame, text="Search by Name", width=75, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.byName)
        odrNumButton = Button(frame, text="Search by Order Number", width=75, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.byOrdNum)
        openButton = Button(frame, text="Search Open Orders", width=75, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.byOpen)
        completeButton = Button(frame, text="Search Completed Orders", width=75, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.byComplete)
        ext = Button(frame, text="Back", padx=50, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: self.ws.destroy())
        nameButton.grid(row=2, column=0, pady=20)
        odrNumButton.grid(row=3, column=0, pady=20)
        openButton.grid(row=4, column=0, pady=20)
        completeButton.grid(row=5, column=0, pady=20)
        ext.grid(row=6, column=0, pady=20)
        self.ws.mainloop()

    def byName(self):
        self.wname = Tk()
        self.wname.title('Search by Name')
        self.wname.geometry('500x400')
        self.wname.config(bg="light gray")
        self.wname.attributes('-fullscreen', True)
        frame = Frame(self.wname, padx=20, pady=20)
        frame.pack(expand=True)
        Label(frame, text="Look-up Current Users by Last Name", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        Label(frame, text='Enter Last Name', font=("Times", "14")).grid(row=1, column=0, pady=5)
        self.lname = Entry(frame, width=30)
        self.lname.grid(row=1, column=1)
        searchButton = Button(frame, text="Submit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.submitName)
        ext = Button(frame, text="Back", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: self.wname.destroy())
        searchButton.grid(row=6, column=1, pady=20)
        ext.grid(row=6, column=2, pady=20)
        self.wname.mainloop()
    def submitName(self):
        lname_check = self.lname.get()
        self.lname.delete(0, END)
        if lname_check == "":
            warn = "Field Cannot be Empty!"
            messagebox.showerror('', warn)
        else:
            check_term = lname_check
            check_Name = "lastName"
            check_ID = "id"
            host = "127.0.0.1"
            port = int(3306)
            user = "root"
            password = "1qaz1qaz!QAZ!QAZ"
            dbname = "shop"
            mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
            cursor = mydb.cursor()
            searchName = "SELECT * FROM user WHERE " + check_Name + " = %s"
            cursor.execute(searchName, check_term)
            resultsUsers = cursor.fetchall()
            for rowUsers in resultsUsers:
                idNum = rowUsers[0]
                searchSQL = "SELECT * FROM shop.order WHERE "+check_ID+" = %s"
                cursor.execute(searchSQL, idNum)
                result = cursor.fetchall()
                for row in result:
                    orderView.Results(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])

            orderView.show_results()

    def byOrdNum(self):
        self.wAcc = Tk()
        self.wAcc.title('Search by Order Number')
        self.wAcc.geometry('500x400')
        self.wAcc.config(bg="light gray")
        self.wAcc.attributes('-fullscreen', True)
        frame = Frame(self.wAcc, padx=20, pady=20)
        frame.pack(expand=True)
        Label(frame, text="Look-up by Order Number", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        Label(frame, text='Enter Order Number', font=("Times", "14")).grid(row=1, column=0, pady=5)
        self.orderNum = Entry(frame, width=30)
        self.orderNum.grid(row=1, column=1)
        searchButton = Button(frame, text="Submit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.submitOrdNum)
        ext = Button(frame, text="Back", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: self.wAcc.destroy())
        searchButton.grid(row=6, column=1, pady=20)
        ext.grid(row=6, column=2, pady=20)
        self.wAcc.mainloop()
    def submitOrdNum(self):
        ordNum_check = self.orderNum.get()
        self.orderNum.delete(0, END)
        if ordNum_check == "":
            warn = "Field Cannot be Empty!"
            messagebox.showerror('', warn)
        else:
            check_term = ordNum_check
            check_for = "id"
            host = "127.0.0.1"
            port = int(3306)
            user = "root"
            password = "1qaz1qaz!QAZ!QAZ"
            dbname = "shop"
            mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
            cursor = mydb.cursor()
            searchSQL = "SELECT * FROM shop.order WHERE "+check_for+" = %s"
            cursor.execute(searchSQL, check_term)
            results = cursor.fetchall()
            for row in results:
                orderView.Results(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
            orderView.show_results()

    def byOpen(self):
        self.wEm = Tk()
        self.wEm.title('Search by Open Orders')
        self.wEm.geometry('500x400')
        self.wEm.config(bg="light gray")
        self.wEm.attributes('-fullscreen', True)
        frame = Frame(self.wEm, padx=20, pady=20)
        frame.pack(expand=True)
        Label(frame, text="Look-up Open Orders", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        searchButton = Button(frame, text="Submit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.submitOpen)
        ext = Button(frame, text="Back", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: self.wEm.destroy())
        searchButton.grid(row=6, column=1, pady=20)
        ext.grid(row=6, column=2, pady=20)
        self.wEm.mainloop()
    def submitOpen(self):
        check_term = 1
        check_for = "status"
        host = "127.0.0.1"
        port = int(3306)
        user = "root"
        password = "1qaz1qaz!QAZ!QAZ"
        dbname = "shop"
        mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
        cursor = mydb.cursor()
        searchSQL = "SELECT * FROM shop.order WHERE "+check_for+" = %s"
        cursor.execute(searchSQL, check_term)
        results = cursor.fetchall()
        for row in results:
            orderView.Results(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        orderView.show_results()

    def byComplete(self):
        self.wEm = Tk()
        self.wEm.title('Search by Complete Orders')
        self.wEm.geometry('500x400')
        self.wEm.config(bg="light gray")
        self.wEm.attributes('-fullscreen', True)
        frame = Frame(self.wEm, padx=20, pady=20)
        frame.pack(expand=True)
        Label(frame, text="Look-up Complete Orders", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        searchButton = Button(frame, text="Submit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.submitComplete)
        ext = Button(frame, text="Back", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: self.wEm.destroy())
        searchButton.grid(row=6, column=1, pady=20)
        ext.grid(row=6, column=2, pady=20)
        self.wEm.mainloop()
    def submitComplete(self):
        check_term = 0
        check_for = "status"
        host = "127.0.0.1"
        port = int(3306)
        user = "root"
        password = "1qaz1qaz!QAZ!QAZ"
        dbname = "shop"
        mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
        cursor = mydb.cursor()
        searchSQL = "SELECT * FROM shop.order WHERE "+check_for+" = %s"
        cursor.execute(searchSQL, check_term)
        results = cursor.fetchall()
        for row in results:
            orderView.Results(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        orderView.show_results()
