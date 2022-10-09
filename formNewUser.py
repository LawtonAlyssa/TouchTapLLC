'''
************************************************************************************************************************
Author: Brandon Romero & Matthew Martinez
Assignment: Software Engineering Project (FORM for NEW Account)
Last Edited: 10/06/2022
Program Description: A GUI window with text entry fields, buttons, and check boxes for adding users to the database
 * Input: Button presses; Strings: First Name, Middle Name, Last Name, Phone Number, eMail, and Password
 * Output: An object containing the new user's information, written to the AWS database
 * Restrictions: No blank entry fields; Passwords must match
************************************************************************************************************************
'''
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import pymysql
import datetime

class newAcc:
    def __call__(self):
        self.ws = Tk()
        self.ws.title('Add New Customer')
        self.ws.geometry('500x400')
        self.ws.config(bg="light gray")
        self.ws.attributes('-fullscreen', True)

        # Frame and Labels
        frame = Frame(self.ws, padx=20, pady=20)
        frame.pack(expand=True)
        Label(frame, text="Create New Account", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        Label(frame, text='First Name', font=("Times", "14")).grid(row=1, column=0, pady=5)
        Label(frame, text='Middle Name', font=("Times", "14")).grid(row=2, column=0, pady=5)
        Label(frame, text='Last Name', font=("Times", "14")).grid(row=3, column=0, pady=5)
        Label(frame, text='Email Address', font=("Times", "14")).grid(row=4, column=0, pady=5)
        Label(frame, text='Phone Number', font=("Times", "14")).grid(row=5, column=0, pady=5)
        Label(frame, text='Ex. xxx-xxx-xxxx', font=("Times", "14")).grid(row=6, column=1, pady=1)
        Label(frame, text='Password', font=("Times", "14")).grid(row=7, column=0, pady=5)
        Label(frame, text='Re-Enter Password', font=("Times", "14")).grid(row=8, column=0, pady=5)

        # Entry Boxes
        self.fname = Entry(frame, width=30)
        self.mname = Entry(frame, width=30)
        self.lname = Entry(frame, width=30)
        self.em = Entry(frame, width=30)
        self.phone = Entry(frame, width=30)
        self.pwd = Entry(frame, width=30)
        self.vpwd = Entry(frame, width=30)
        self.fname.grid(row=1, column=1)
        self.mname.grid(row=2, column=1)
        self.lname.grid(row=3, column=1)
        self.em.grid(row=4, column=1)
        self.phone.grid(row=5, column=1)
        self.pwd.grid(row=7, column=1)
        self.vpwd.grid(row=8, column=1)
        self.varAdmin = tk.IntVar()
        self.c1 = tk.Checkbutton(frame, text='ADMIN', variable=self.varAdmin, onvalue=1, offvalue=0)
        self.c1.grid(row=10, column=1)


        # Buttons
        clr = Button(frame, text="Clear", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.clear)
        reg = Button(frame, text="Register", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.submit)
        ext = Button(frame, text="Back", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: self.ws.destroy())
        clr.grid(row=11, column=0, pady=20)
        reg.grid(row=11, column=1, pady=20)
        ext.grid(row=11, column=2, pady=20)

        self.ws.mainloop()
    def submit(self):
        fname_check = self.fname.get()
        mname_check = self.mname.get()
        lname_check = self.lname.get()
        em_check = self.em.get()
        phone_check = self.phone.get()
        pwd_check = self.pwd.get()
        vpwd_check = self.vpwd.get()
        admin_check = self.varAdmin.get()
        current_time = datetime.datetime.now()
        yyyy = str(current_time.year)
        mm = str(current_time.month)
        dd = str(current_time.day)
        hh = str(current_time.hour)
        m_m = str(current_time.minute)
        ss = str(current_time.second)

        date_time = yyyy+'-'+mm+'-'+dd+' '+hh+':'+m_m+':'+ss
        check_count = 0
        if pwd_check != vpwd_check:
            warn = "Passwords Do not Match!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if fname_check == "":
            warn = "First name can't be empty!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if mname_check == "":
            warn = "Middle name can't be empty!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if lname_check == "":
            warn = "Last name can't be empty!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if em_check == "":
            warn = "Email can't be empty!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if phone_check == "":
            warn = "Phone Number can't be empty!"
            messagebox.showerror('', warn)
        else:
            check_count += 1
        if pwd_check == "":
            warn = "Password can't be empty!"
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
            firstName = self.fname.get()
            middleName = self.mname.get()
            lastName = self.lname.get()
            eMail = self.em.get()
            phoneNum = self.phone.get()
            Password = self.pwd.get()
            new_customer = ('0', firstName, middleName, lastName, phoneNum, eMail, Password, admin_check, date_time, date_time)
            cursor.execute('INSERT INTO user VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                           (new_customer[0], new_customer[1], new_customer[2], new_customer[3], new_customer[4], new_customer[5], new_customer[6], new_customer[7], new_customer[8], new_customer[9]))
            mydb.commit()
            self.ws.destroy()
        else:
            warn = "An unknown error occurred!"
            messagebox.showerror('', warn)
    def clear(self):
        self.fname.delete(0, END)
        self.mname.delete(0, END)
        self.lname.delete(0, END)
        self.em.delete(0, END)
        self.phone.delete(0, END)
        self.pwd.delete(0, END)
        self.vpwd.delete(0, END)
        self.varAdmin.set(0)
        self.c1.deselect()
