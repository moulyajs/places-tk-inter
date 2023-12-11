from tkinter import *
from tkinter import messagebox

import sqlite3

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

img = PhotoImage(file='images/agra.png')
Label(root, image=img, border=0, bg='white').place(x=50, y=90)
Button(root, width=39, pady=7, text='Sign in',
       bg='#57a1f8', fg='white', border=0).place(x=35, y=300)


def query():

    conn = sqlite3.connect('adress_book.bd')

    c = conn.cursor()
    c.execute("SELECT*,oid FROM addresses")

    conn.commit()
    conn.close()


root.mainloop()
