from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

#dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
namn = ['Fredde']
id_nr = [1]
questions_done = [20]
correct_answers = [13]
#dt.strftime("%A, %d. %B %Y %I:%M%p")

class Startsida(tk.Tk):
    """Förstan sidan - frame"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        #__init__(self, parent, *args, **kwargs):
        #super().__init__(parent, *args, **kwargs)
        self.name = tk.StringVar()
        self.showhistory()

    def addtodatabas(self):
        #great_work = ttk.Label(self, text="Bra jobbat!")
        #great_work.grid(row=4, column=4)
        huvud_rakning = sqlite3.connect("Test_databas_A.db")
        cursor = huvud_rakning.cursor()

        namn1 = namn
        #id_nr1 = id_nr
        antalg = sum(questions_done)
        points = sum(correct_answers)
        procent = [(points/antalg)*100]
        d_bas = [(f'{d1}', f'{namn1}', f'{antalg}', f'{points}', f'{procent}')]

        #print(d_bas)
        cursor.execute("CREATE TABLE if not exists resultat(ID INT, datum DATE, namn TEXT, Antalgjorda INT, Points INT, procent INT)")
        #SELECT: datetime('now')
        cursor.executemany("INSERT INTO resultat VALUES(?,?,?,?,?,?);", d_bas)
        huvud_rakning.commit()

        with sqlite3.connect("Test_databas_A.db") as huvud_rakning:
            cursor = huvud_rakning.cursor()
            cursor.execute("SELECT rowid, * FROM resultat;")
            rubrik = ['ID', 'datum', 'Namn', 'Antalgjorda', 'Points', 'procent']
            print(f'{rubrik[0]:<20}{rubrik[1]:<20}{rubrik[2]}{rubrik[3]:<20}{rubrik[4]:<20}{rubrik[5]}')
            print('-' * 45)
            for row in cursor.fetchall():
                print(f"{row[0]:<20}{row[1]:<20}{row[2]}{row[3]:<20}{row[4]:<20}{row[5]}")


    def showhistory(self):
        self.addtodatabas()
        #win = Tk()
        #win.title('Översikt')
        #win.geometry('600x1200')

        with sqlite3.connect("Test_databas_A.db") as huvud_rakning:
            tree = ttk.Treeview(column=('ID','Datum','Namn', 'Antal gjorda', 'Antal rätt','Procent'), show='headings')
            tree.column("#1", anchor=CENTER)
            tree.heading("#1", text="ID")
            tree.column("#2", anchor=CENTER)
            tree.heading("#2", text="Datum")
            tree.column("#3", anchor=CENTER)
            tree.heading("#3", text="Namn")
            tree.column("#4", anchor=CENTER)
            tree.heading("#4", text="Antal gjorda")
            tree.column("#5", anchor=CENTER)
            tree.heading("#5", text="Antal rätt")
            tree.column("#6", anchor=CENTER)
            tree.heading("#6", text="Procent")
            tree.pack(fill=BOTH, expand=1)

        with sqlite3.connect("Test_databas_A.db"):
            cursor = huvud_rakning.cursor()
            cursor.execute("SELECT rowid, * FROM resultat;")
            rows = cursor.fetchall()
            for row in rows:
                #print(row)
                tree.insert("", END, values=row)

class MyApplication(tk.Tk):
    #Huvud applikationen
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

        self.title("Huvudräkningsträning")
        self.geometry("600x600")
        self.resizable(width=False, height=False)

        Startsida(self).grid(sticky=(tk.E+tk.W+tk.N+tk.S))
        self.columnconfigure(1, weight=1)

if __name__ =='__main__':
    app = Startsida()
    app.mainloop()

