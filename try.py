"""from tkinter import *
from transportation import facilities
root = Tk()
root.title('Places to visit')
root.geometry('925x700+300+200')
root.configure(bg='#fff')
root.resizable(True, True)

sign_up = Button(root, width=6, text='Sign Up', border=0,
                 bg='#57a1f8', fg='white', command=facilities)
sign_up.place(x=215, y=270)
root.mainloop()"""
from tkinter import *
from finalplaces import places
from transportation import facilities
main = Tk()
main.title("Voyageur")
main.geometry('1400x800')
main.configure(bg='beige')

heading1 = Label(main, text='VOYAGEUR', font=(
    "Tahoma", 40, "bold italic"), bg='beige', width=40)
heading2 = Label(main, text='TRAVEL AND TOURISM MANAGEMENT',
                 font=("Courier New", 22, "italic"), bg='beige')

heading1.pack()
heading2.pack()

f1 = Button(main, text='Translator', width=20, height=5,
            font=("Helvetica", 16, 'bold italic'), relief=FLAT)  # f1 = Translator
f2 = Button(main, text='History', width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT)  # f2 = History
f3 = Button(main, text='Diversity', width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT)  # f3 = Diversity
f4 = Button(main, text='Booking', width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT)  # f4 = Booking
f5 = Button(main, text='Accomodation', width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT)  # f5 = Accomodation
f6 = Button(main, text='Food', width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT)  # f6 = Food
f7 = Button(main, text='Shopping', width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT)  # f7 = Shopping
f8 = Button(main, text='Transportation', width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT, command=facilities)  # f8 = Transportation
f9 = Button(main, text='Places To Visit', width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT, command=places)  # f9 = Places to Visit
f10 = Button(main, text='Rating', width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT)  # f9 = Places to Visit
f11 = Button(main, text='Common Building', width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT)  # f9 = Places to Visit
f12 = Button(main, text='Events', width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT)  # f9 = Places to Visit

f1.place(x=40, y=150)
f2.place(x=340, y=150)
f3.place(x=640, y=150)
f4.place(x=940, y=150)
f5.place(x=40, y=350)
f6.place(x=340, y=350)
f7.place(x=640, y=350)
f8.place(x=940, y=350)
f9.place(x=40, y=550)
f10.place(x=340, y=550)
f11.place(x=640, y=550)
f12.place(x=940, y=550)

main.mainloop()
# ,font = ("Helvetica",16,'bold')
