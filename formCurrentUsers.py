'''
************************************************************************************************************************
Author: Brandon Romero & Matthew Martinez
Assignment: Software Engineering Project (FORM for searching current customers)
Last Edited: 8/25/2022
Program Description: A GUI window to perform a search of user accounts stored within the database
 * Input: Selection of query type based on button presses. Search performed using string input provided by user
 * Output: A list containing the results of the query
************************************************************************************************************************
'''
from tkinter import *
from tkinter import messagebox
import pymysql
import userView

class currentAcc:
    def __init__(self):
        self.phone = None
        self.email = None
        self.accNum = None
        self.lname = None
    def __call__(self):
        self.ws = Tk()
        self.ws.title('Search Current Customer')
        self.ws.geometry('500x400')
        self.ws.config(bg="light gray")
        self.ws.attributes('-fullscreen', True)

        # Frame and Labels
        frame = Frame(self.ws, padx=20, pady=20)
        frame.pack(expand=True)
        Label(frame, text="Look-up Current Users", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)

        # Buttons
        nameButton = Button(frame, text="Search by Name", width=75, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.byName)
        accButton = Button(frame, text="Search by Account Number", width=75, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.byAccNum)
        emailButton = Button(frame, text="Search by Email", width=75, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.byEmail)
        phoneButton = Button(frame, text="Search by Phone Number", width=75, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.byPhone)
        ext = Button(frame, text="Back", padx=50, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: self.ws.destroy())

        nameButton.grid(row=2, column=0, pady=20)
        accButton.grid(row=3, column=0, pady=20)
        emailButton.grid(row=4, column=0, pady=20)
        phoneButton.grid(row=5, column=0, pady=20)
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
            check_for = "lastName"
            host = "127.0.0.1"
            port = int(3306)
            user = "root"
            password = "1qaz1qaz!QAZ!QAZ"
            dbname = "shop"
            mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
            cursor = mydb.cursor()
            searchSQL = "SELECT * FROM user WHERE "+check_for+" = %s"
            cursor.execute(searchSQL, check_term)
            results = cursor.fetchall()
            for row in results:
                userView.Results(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            userView.show_results()
    def byAccNum(self):
        self.wAcc = Tk()
        self.wAcc.title('Search by Account Number')
        self.wAcc.geometry('500x400')
        self.wAcc.config(bg="light gray")
        self.wAcc.attributes('-fullscreen', True)
        frame = Frame(self.wAcc, padx=20, pady=20)
        frame.pack(expand=True)
        Label(frame, text="Look-up Current Users by Account Number", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        Label(frame, text='Enter Account Number', font=("Times", "14")).grid(row=1, column=0, pady=5)
        self.accNum = Entry(frame, width=30)
        self.accNum.grid(row=1, column=1)
        searchButton = Button(frame, text="Submit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.submitAccNum)
        ext = Button(frame, text="Back", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: self.wAcc.destroy())
        searchButton.grid(row=6, column=1, pady=20)
        ext.grid(row=6, column=2, pady=20)
        self.wAcc.mainloop()
    def submitAccNum(self):
        accNum_check = self.accNum.get()
        self.accNum.delete(0, END)
        if accNum_check == "":
            warn = "Field Cannot be Empty!"
            messagebox.showerror('', warn)
        else:
            check_term = accNum_check
            check_for = "id"
            host = "127.0.0.1"
            port = int(3306)
            user = "root"
            password = "1qaz1qaz!QAZ!QAZ"
            dbname = "shop"
            mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
            cursor = mydb.cursor()
            searchSQL = "SELECT * FROM user WHERE "+check_for+" = %s"
            cursor.execute(searchSQL, check_term)
            results = cursor.fetchall()
            for row in results:
                userView.Results(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            userView.show_results()
    def byEmail(self):
        self.wEm = Tk()
        self.wEm.title('Search by Name')
        self.wEm.geometry('500x400')
        self.wEm.config(bg="light gray")
        self.wEm.attributes('-fullscreen', True)
        frame = Frame(self.wEm, padx=20, pady=20)
        frame.pack(expand=True)
        Label(frame, text="Look-up Current Users by Email", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        Label(frame, text='Enter Email', font=("Times", "14")).grid(row=1, column=0, pady=5)
        self.email = Entry(frame, width=30)
        self.email.grid(row=1, column=1)
        searchButton = Button(frame, text="Submit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.submitEmail)
        ext = Button(frame, text="Back", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: self.wEm.destroy())
        searchButton.grid(row=6, column=1, pady=20)
        ext.grid(row=6, column=2, pady=20)
        self.wEm.mainloop()
    def submitEmail(self):
        email_check = self.email.get()
        self.email.delete(0, END)
        if email_check == "":
            warn = "Field Cannot be Empty!"
            messagebox.showerror('', warn)
        else:
            check_term = email_check
            check_for = "email"
            host = "127.0.0.1"
            port = int(3306)
            user = "root"
            password = "1qaz1qaz!QAZ!QAZ"
            dbname = "shop"
            mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
            cursor = mydb.cursor()
            searchSQL = "SELECT * FROM user WHERE "+check_for+" = %s"
            cursor.execute(searchSQL, check_term)
            results = cursor.fetchall()
            for row in results:
                userView.Results(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            userView.show_results()
    def byPhone(self):
        self.wPh = Tk()
        self.wPh.title('Search by Name')
        self.wPh.geometry('500x400')
        self.wPh.config(bg="light gray")
        self.wPh.attributes('-fullscreen', True)
        frame = Frame(self.wPh, padx=20, pady=20)
        frame.pack(expand=True)
        Label(frame, text="Look-up Current Users by Phone Number", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        Label(frame, text='Enter Phone Number', font=("Times", "14")).grid(row=1, column=0, pady=5)
        Label(frame, text='Ex. xxx-xxx-xxxx', font=("Times", "14")).grid(row=5, column=0, pady=5)
        self.phone = Entry(frame, width=30)
        self.phone.grid(row=1, column=1)
        searchButton = Button(frame, text="Submit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.submitPhone)
        ext = Button(frame, text="Back", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: self.wPh.destroy())
        searchButton.grid(row=6, column=1, pady=20)
        ext.grid(row=6, column=2, pady=20)
        self.wPh.mainloop()
    def submitPhone(self):
        phone_check = self.phone.get()
        self.phone.delete(0, END)
        if phone_check == "":
            warn = "Field Cannot be Empty!"
            messagebox.showerror('', warn)
        else:
            check_term = phone_check
            check_for = "mobile"
            host = 'softwareproject.cxtf7fowbhbj.us-east-1.rds.amazonaws.com'
            port = int(3306)
            user = 'admin'
            password = '1qaz1qaz!QAZ!QAZ'
            dbname = 'shop'
            mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
            cursor = mydb.cursor()
            searchSQL = "SELECT * FROM user WHERE "+check_for+" = %s"
            cursor.execute(searchSQL, check_term)
            results = cursor.fetchall()
            for row in results:
                userView.Results(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            userView.show_results()
