from tkinter import *
from tkinter import messagebox
from finalplaces import places
from transportation import facilities
from Voyageur_main import booking, rating, events, healthaid, create_translator, history_print, diversity_print
from Voyageur_main import accommodation, FOODS, Shopping

# import ast
import sqlite3

root = Tk()
root.title('VOYAGEUR')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(True, True)


def signin():
    username = user.get()
    password = code.get()
    # file = open('datasheet.txt', 'r')
    # d = file.read()
    # r = ast.literal_eval(d)
    # file.close()
    try:
        with sqlite3.connect('places.db') as db_con:
            # db_con = sqlite3.connect('places.db')
            db_cursor = db_con.cursor()
            db_cursor.execute("SELECT * FROM users WHERE name='"+username+"'")
            result = db_cursor.fetchall()
    # print(result)
            #conn.commit()
    # conn.close()
   # print(r.keys())
   # print(r.values())

    # if username in r.keys() and password == r[username]:
        for i in result:
            list(i)
            if i[1] == username and i[2] == password:

                main = Toplevel()
                main.title("Voyageur")
                main.geometry('1400x800')
                main.configure(bg='beige')

                heading1 = Label(main, text='VOYAGEUR', font=(
                    "Tahoma", 40, "bold italic"), bg='beige', width=40)
                heading2 = Label(main, text='TRAVEL AND TOURISM MANAGEMENT',
                                 font=("Courier New", 22, "italic"), bg='beige')

                heading1.pack()
                heading2.pack()

                def button_creation(functionality, function, colour, a, b):
                    p = Button(main, text=functionality, fg=colour, command=function, width=20,
                               height=5, font=("Helvetica", 16, 'bold italic'), relief=FLAT, bg='beige')
                    return p.place(x=a, y=b)
        db_con.commit()
# dark turqouise - #1EBCAD
# dark emerald green - #00C800
# orchid purple - DA70D6
# coral - type of orange

                f1 = button_creation(
                    'Translator', create_translator, '#00C800', 940, 550)
                f2 = button_creation(
                    'History', history_print, '#00C800', 640, 150)
                f3 = button_creation(
                    'Diversity', diversity_print, '#00C800', 340, 150)
                f4 = button_creation('Booking', booking, '#1EBCAD', 40, 350)
                f5 = button_creation(
                    'Accomodation', accommodation, '#1EBCAD', 640, 350)
                f6 = button_creation('Food', FOODS, '#1EBCAD', 340, 550)
                f7 = button_creation('Shopping', Shopping, '#DA70D6', 640, 550)
                f8 = button_creation(
                    'Transportation', facilities, '#DA70D6', 340, 350)
                f9 = button_creation(
                    'Places To Visit', places, '#DA70D6', 940, 150)
                f10 = button_creation('Rating', rating, 'coral', 940, 350)
                f11 = button_creation(
                    'Health Aid', healthaid, 'coral', 40, 150)
                f12 = button_creation('Events', events, 'coral', 40, 550)

                main.mainloop()

            else:
                messagebox.showerror('Invalid', 'invalid username or password')
# ----------------------------------------------------------------------------------
    except Exception as e:
        messagebox.showerror('Invalid', e)


def signup_command():
    window = Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(True, True)

    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()
        try:
            # file = open('datasheet.txt', 'r+')
            # d = file.read()
            # r = ast.literal_eval(d)

            # dict2 = {username: password}
            # r.update(dict2)
            # file.truncate(0)
            # file.close()

            # file = open('datasheet.txt', 'w')
            # file.write(str(r))
            if password != confirm_password:
                raise Exception("Both passwords should match")

            db_con = sqlite3.connect('places.db')
            db_cursor = db_con.cursor()
            db_cursor.execute(
                "SELECT * FROM users WHERE name='"+username+"'")
            existing_user = db_cursor.fetchall()

            if len(existing_user) > 0:
                raise Exception("User already exists")
            db_cursor.execute(
                "INSERT INTO users (name,password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()

            messagebox.showinfo('Signup', 'Successfully sign up')
            window.destroy()
        except BaseException as e:
            # file = open('datasheet.txt', 'w')
            # pp = str({'Username': 'password'})
            # file.write(pp)
            # file.close()
            messagebox.showerror('Invalid', e)

    def sign():
        window.destroy()

    img = PhotoImage(file='signup1.png')
    Label(window, image=img, border=0, bg='white').place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white',
                    font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

# -------------------------------------------------------------

    def on_enter_hi(e):
        user.delete(0, 'end')

    def on_leave_hi(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=2,
                 bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')

    user.bind("<FocusIn>", on_enter_hi)
    user.bind("<FocusOut>", on_leave_hi)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# ---------------------------------------------------------------

    def on_enter_hello(e):
        code.delete(0, 'end')

    def on_leave_hello(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg='black', border=2,
                 bg='white', font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')

    code.bind("<FocusIn>", on_enter_hello)
    code.bind("<FocusOut>", on_leave_hello)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# ---------------------------------------------------------------

    def on_enter(e):
        confirm_code.delete(0, 'end')

    def on_leave(e):
        name = confirm_code.get()
        if name == '':
            confirm_code.insert(0, 'Confirm Password')

    confirm_code = Entry(frame, width=25, fg='black', border=2,
                         bg='white', font=('Microsoft Yahei UI Light', 11))
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, 'Confirm Password')

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
    confirm_code.bind("<FocusIn>", on_enter)
    confirm_code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

# ---------------------------------------------------------------

    Button(frame, width=39, pady=7, text='Sign up',
           bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
    label = Label(frame, text='I have an account', fg='black',
                  bg='white', font=('Microsoft Yahei UI Light', 9))
    label.place(x=90, y=340)

    signin = Button(frame, width=6, text='Sign in', border=0,
                    bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    signin.place(x=200, y=340)

    window.mainloop()


# ---------------------------------------------------------------------------------------
img = PhotoImage(file='images/final.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI light', 23, 'bold'))
heading.place(x=100, y=5)

# ----------------------------------------------------------


def on_enter_b(e):
    user.delete(0, 'end')


def on_leave_b(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=39, fg='black', border=2,
             bg='white', font=('Microsoft YaHei UI light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_b)
user.bind('<FocusOut>', on_leave_b)


# Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# ------------------------------------------------------------


def on_enter_a(e):
    code.delete(0, 'end')


def on_leave_a(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


code = Entry(frame, width=39, fg='black', border=2,
             bg='white', font=('Microsoft YaHei UI light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter_a)
code.bind('<FocusOut>', on_leave_a)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# -------------------------------------------------------------

Button(frame, width=39, pady=7, text='Sign in',
       bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have a account?", fg='black',
              bg='white', font=('Microsoft YaHei UI light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign Up', border=0,
                 bg='white', cursor='hand2', fg='#57a1f8', command=signup_command)
sign_up.place(x=215, y=270)

# database connection initializing

conn = sqlite3.connect('places.db')

# cursor
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE IF NOT EXISTS users (id  INTEGER NOT NULL PRIMARY KEY,name VARCHAR(128) NOT NULL,password VARCHAR(128) NOT NULL
)""")


# curson commt
conn.commit()


root.mainloop()

# close the database connection

conn.close()
