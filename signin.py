from tkinter import *
from tkinter import messagebox
# import ast
import sqlite3

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)


def signin():
    username = user.get()
    password = code.get()
    # file = open('datasheet.txt', 'r')
    # d = file.read()
    # r = ast.literal_eval(d)
    # file.close()
    db_con = sqlite3.connect('places.db')
    db_cursor = db_con.cursor()
    db_cursor.execute("SELECT * FROM users WHERE name='"+username+"'")
    result = db_cursor.fetchall()
    # print(result)
    conn.commit()
    # conn.close()
   # print(r.keys())
   # print(r.values())

    # if username in r.keys() and password == r[username]:
    for i in result:
        list(i)
        if i[1] == username and i[2] == password:

            screen = Toplevel(root)
            screen.title("App")
            screen.geometry('925x500+300+200')
            screen.config(bg="white")

            Label(screen, text="Hello everyone!!!", bg='#fff', font=(
                'Calibri(body)', 50, 'bold')).pack(expand=True)
            screen.mainloop()

        else:
            messagebox.showerror('Invalid', 'invalid username or password')
# ----------------------------------------------------------------------------------


def signup_command():
    window = Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)

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
