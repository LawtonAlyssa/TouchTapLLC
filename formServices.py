'''
************************************************************************************************************************
Author: Brandon Romero & Matthew Martinez
Assignment: Software Engineering Project (FORM for viewing services)
Last Edited: 8/25/2022
Program Description: A GUI window to perform a search of products/services stored within the database
 * Input: Selection based query where buttons are pressed to perform a query
 * Output: A list containing the results of the query
************************************************************************************************************************
'''
from tkinter import *
import pymysql
import productView

class viewServices:
    def __call__(self):
        self.ws = Tk()
        self.ws.title('Services')
        self.ws.geometry('500x400')
        self.ws.config(bg="light gray")
        self.ws.attributes('-fullscreen', True)

        # Frame and Labels
        frame = Frame(self.ws, padx=20, pady=20)
        frame.pack(expand=True)
        Label(frame, text="Select a Service to View Details", font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)

        # Buttons
        brailleT = Button(frame, text="Literature Transcription", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.brailleLit)
        brailleM = Button(frame, text="Math Transcription", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.brailleMath)
        impWalk = Button(frame, text="Mobility Lessons", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=self.mobility)
        ext = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda: self.ws.destroy())
        brailleT.grid(row=6, column=0, pady=20)
        brailleM.grid(row=6, column=1, pady=20)
        impWalk.grid(row=6, column=2, pady=20)
        ext.grid(row=6, column=3, pady=20)

        self.ws.mainloop()
    def brailleLit(self):
        check_term = 'Literature'
        check_for = "metaTitle"
        host = "127.0.0.1"
        port = int(3306)
        user = "root"
        password = "1qaz1qaz!QAZ!QAZ"
        dbname = "shop"
        mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
        cursor = mydb.cursor()
        searchSQL = "SELECT * FROM shop.product WHERE " + check_for + " = %s"
        cursor.execute(searchSQL, check_term)
        results = cursor.fetchall()
        for row in results:
            productView.Results(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        productView.show_results()
    def brailleMath(self):
        check_term = 'Math'
        check_for = "metaTitle"
        host = "127.0.0.1"
        port = int(3306)
        user = "root"
        password = "1qaz1qaz!QAZ!QAZ"
        dbname = "shop"
        mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
        cursor = mydb.cursor()
        searchSQL = "SELECT * FROM shop.product WHERE " + check_for + " = %s"
        cursor.execute(searchSQL, check_term)
        results = cursor.fetchall()
        for row in results:
            productView.Results(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        productView.show_results()
    def mobility(self):
        check_term = 'Lesson'
        check_for = "metaTitle"
        host = "127.0.0.1"
        port = int(3306)
        user = "root"
        password = "1qaz1qaz!QAZ!QAZ"
        dbname = "shop"
        mydb = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port)
        cursor = mydb.cursor()
        searchSQL = "SELECT * FROM shop.product WHERE " + check_for + " = %s"
        cursor.execute(searchSQL, check_term)
        results = cursor.fetchall()
        for row in results:
            productView.Results(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        productView.show_results()


