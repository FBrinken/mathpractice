from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import sqlite3
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

correct_answers = []
questions_done = []
namn = []
raknesatt = ['Huvudräkning']


class Startsida(ttk.Frame):
    """Förstan sidan - frame"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set("Hej! Skriv ditt namn i rutan.")
        self.namn1 = tk.StringVar()

        #self.showhistory()

        name_label = ttk.Label(self, text="Namn:")
        name_entry =  ttk.Entry(self, textvariable=self.name)
        ch_button = ttk.Button(self, text="Enter", command=self.on_change)
        hello_label = ttk.Label(self, textvariable=self.hello_string, font=("TkDefaultFont", 40),wraplength=600)
        #klicka_for_historik = ttk.Button(self, text="Klicka för historik", command=self.showhistory)

        #klicka_for_historik.grid(row=6, column=0)
        name_label.grid(row=1, column=0, sticky=tk.W)
        name_entry.grid(row=1, column=1)
        ch_button.grid(row=1, column=2, sticky=tk.E)
        hello_label.grid(row=0, column=0, columnspan=3)

        self.columnconfigure(1, weight=1, pad=2)

    def on_change(self):
        if self.name.get().strip():
            self.namn1 = self.name.get()
            namn.insert(0, self.namn1)
            print(namn)
            self.hello_string.set("Hej " + self.name.get())

            question_label = ttk.Label(self, text="Vad vill du träna på?")
            addition_button = ttk.Button(self, text="Addition", command=self.clearframe_a)
            subtraktion_button = ttk.Button(self, text="Subtraktion", command=self.clearframe_s)
            multiplikation_button = ttk.Button(self, text="Multiplikation", command=self.clearframe_m)
            dividing_button = ttk.Button(self, text="Division", command=self.clearframe_d)


            question_label.grid(row=2, column=0, sticky=tk.W)
            addition_button.grid(row=3, column=0, sticky=tk.W)
            subtraktion_button.grid(row=3, column=1, sticky=tk.W)
            multiplikation_button.grid(row=3, column=2, sticky=tk.W)
            dividing_button.grid(row=3, column=3, sticky=tk.W)

        else:
            self.hello_string.set("Hej! Skriv in ditt namn i rutan.")

    def clearframe_a(self): #Rensa allt inom framen innan addition
        for widget in Startsida.winfo_children(self):
            widget.destroy()
            self.addition()
    def clearframe_s(self): #Rensa allt inom framen innan addition
        for widget in Startsida.winfo_children(self):
            widget.destroy()
            self.subtraktion()
    def clearframe_m(self): #Rensa allt inom framen innan addition
        for widget in Startsida.winfo_children(self):
            widget.destroy()
            self.multiplikation()
    def clearframe_d(self): #Rensa allt inom framen innan addition
        for widget in Startsida.winfo_children(self):
            widget.destroy()
            self.dividing()


    def avsluta(self): #avsluta programmet och spara till databasen innan
        #self.addtodatabas()
        exit()

    def addition(self): #fylla o definiera variabler
            raknesatt[0] = "+"
            value1 = random.randrange(11, 20)
            value2 = random.randrange(1, 10)
            term1 = value1
            term2 = value2
            term_1 = str(term1)
            term_2 = str(term2)

            def kontroll(): #hämtar anv svar och kontrollerar, och lägger in i olika listor
                players_answer = int(players_answer___.get())
                answer = int(value1 + value2)
                players_answer___.delete(0, END)

                if players_answer == answer:
                    correct_answers.append(1)
                    questions_done.append(1)
                    correct_answer = ttk.Label(self, text="Rätt!")
                    correct_answer.grid(row=3, column=3)
                    #print nedan är för min egen kontroll i terminalen
                    print(sum(correct_answers))
                    print(sum(questions_done))
                    print(namn)
                    self.addition() #startar om addition
                else:
                    questions_done.append(1)
                    correct_answer = ttk.Label(self, text="Fel!")
                    correct_answer.grid(row=3, column=3)
                    print(sum(questions_done))
                    self.addition()

            addition____title = ttk.Label(self, text="Addition", font=("TkDefaultFont", 30), wraplength=300)
            addition_subtitle = ttk.Label(self, text="term + term = summa")
            addition_question = ttk.Label(self, text="Vad är summan av " + term_1 + " och " + term_2)
            players_answer___ = ttk.Entry(self, width=12)

            klicka_for___svar = ttk.Button(self, text="Klicka för svar", command=kontroll)
            next_question = ttk.Button(self, text="Avsluta", command=self.avsluta)
            #klicka_for_summering = ttk.Button(self, text="Klicka för summering", command=self.addtodatabas)
            klicka_for_historik = ttk.Button(self, text="Klicka för historik", command=self.showhistory)

            klicka_for___svar.grid(row=5, column=0, columnspan=5)
            next_question.grid(row=9, column=0, columnspan=5)
            #klicka_for_summering.grid(row=7, column=0, columnspan=5)
            klicka_for_historik.grid(row=8, column=0, columnspan=5)

            addition____title.grid(row=0, column=0, columnspan=5)
            addition_subtitle.grid(row=1, column=0, columnspan=5)
            addition_question.grid(row=2, column=0, columnspan=5)
            players_answer___.grid(row=3, column=0, columnspan=5)

    def subtraktion(self): #fylla o definiera variabler
            raknesatt[0] = "-"
            value1 = random.randrange(11, 20)
            value2 = random.randrange(1, 10)
            term1 = value1
            term2 = value2
            term_1 = str(term1)
            term_2 = str(term2)

            def kontroll(): #hämtar anv svar och kontrollerar, och lägger in i olika listor
                players_answer = int(players_answer___.get())
                answer = int(value1 - value2)
                players_answer___.delete(0, END)

                if players_answer == answer:
                    correct_answers.append(1)
                    questions_done.append(1)
                    correct_answer = ttk.Label(self, text="Rätt!")
                    correct_answer.grid(row=3, column=3)
                    #print nedan är för min egen kontroll i terminalen
                    print(sum(correct_answers))
                    print(sum(questions_done))
                    print(namn)
                    self.subtraktion() #startar om addition
                else:
                    questions_done.append(1)
                    correct_answer = ttk.Label(self, text="Fel!")
                    correct_answer.grid(row=3, column=3)
                    print(sum(questions_done))
                    self.subtraktion()

            addition____title = ttk.Label(self, text="Subtraktion", font=("TkDefaultFont", 30), wraplength=300)
            addition_subtitle = ttk.Label(self, text="term + term = differens")
            addition_question = ttk.Label(self, text="Vad är differensen mellan " + term_1 + " och " + term_2)
            players_answer___ = ttk.Entry(self, width=12)

            klicka_for___svar = ttk.Button(self, text="Klicka för svar", command=kontroll)
            next_question = ttk.Button(self, text="Avsluta", command=self.avsluta)
            #klicka_for_summering = ttk.Button(self, text="Klicka för summering", command=self.addtodatabas)
            klicka_for_historik = ttk.Button(self, text="Klicka för historik", command=self.showhistory)

            klicka_for___svar.grid(row=5, column=0, columnspan=5)
            next_question.grid(row=9, column=0, columnspan=5)
            #klicka_for_summering.grid(row=7, column=0, columnspan=5)
            klicka_for_historik.grid(row=8, column=0, columnspan=5)

            addition____title.grid(row=0, column=0, columnspan=5)
            addition_subtitle.grid(row=1, column=0, columnspan=5)
            addition_question.grid(row=2, column=0, columnspan=5)
            players_answer___.grid(row=3, column=0, columnspan=5)

    def addtodatabas(self):
        great_work = ttk.Label(self, text="Bra jobbat!")
        great_work.grid(row=4, column=4)
        huvud_rakning = sqlite3.connect("Shire.db")
        cursor = huvud_rakning.cursor()

        #namn1 = namn
        antalg = sum(questions_done)
        points = sum(correct_answers)
        procenten = round((points/antalg)*100)
        d_bas = [(f'{d1}', f'{namn}', f'{raknesatt}', f'{procenten}', f'{antalg}', f'{points}')]


        print(d_bas)
        cursor.execute("CREATE TABLE if not exists resultat3(""Datum TEXT, Namn TEXT, Räknesätt TEXT, Procent INT, Antalg INT, Points INT)")
        cursor.executemany("INSERT INTO resultat3 VALUES(?, ?, ?, ?, ?, ?);", d_bas)
        huvud_rakning.commit()

        # with sqlite3.connect("Shire.db") as huvud_rakning:
        #     cursor = huvud_rakning.cursor()
        #     cursor.execute("SELECT rowid, * FROM resultat1;")
        #     rubrik = ['Namn', 'Antal frågor', 'Antal rätt']
        #     print(f'{rubrik[0]:<20}{rubrik[1]:<20}{rubrik[2]}')
        #     print('-' * 45)
        #     for row in cursor.fetchall():
        #         print(f"{row[0]:<20}{row[1]:<20}{row[2]}")

    def showhistory(self):
        self.addtodatabas()
        win = Tk()
        win.title('Översikt')
        win.geometry('1200x1200')

        with sqlite3.connect("Shire.db") as huvud_rakning:
            tree = ttk.Treeview(win, column=('ID', 'Datum', 'Namn', 'Räknesätt', 'Andel rätt i %', 'Antal frågor', 'Antal rätt'),
                                show='headings')
            tree.column("#1", anchor=CENTER)
            tree.heading("#1", text="ID")
            tree.column("#2", anchor=CENTER)
            tree.heading("#2", text="Datum")
            tree.column("#3", anchor=CENTER)
            tree.heading("#3", text="Namn")
            tree.column("#4", anchor=CENTER)
            tree.heading("#4", text="Räknesätt")
            tree.column("#5", anchor=CENTER)
            tree.heading("#5", text="Andel rätt i %")
            tree.column("#6", anchor=CENTER)
            tree.heading("#6", text="Antal frågor")
            tree.column("#7", anchor=CENTER)
            tree.heading("#7", text="Rätta svar")
            tree.grid(sticky=(tk.E+tk.W+tk.N+tk.S))#pack(fill=BOTH, expand=1)

        with sqlite3.connect("Shire.db"):
            cursor = huvud_rakning.cursor()
            cursor.execute("SELECT rowid, * FROM resultat3;")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
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
    app = MyApplication()
    app.mainloop()