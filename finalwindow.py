from tkinter import *
from finalplaces import places
from transportation import facilities
from Voyageur_main import booking, rating, events, healthaid, create_translator, history_print, diversity_print
from Voyageur_main import accommodation, FOODS, Shopping

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


def button_creation(functionality, function, colour, a, b):
    p = Button(main, text=functionality, fg=colour, command=function, width=20,
               height=5, font=("Helvetica", 16, 'bold italic'), relief=FLAT, bg='beige')
    return p.place(x=a, y=b)

# dark turqouise - #1EBCAD
# dark emerald green - #00C800
# orchid purple - DA70D6
# coral - type of orange


f1 = button_creation('Translator', create_translator, '#00C800', 940, 550)
f2 = button_creation('History', history_print, '#00C800', 640, 150)
f3 = button_creation('Diversity', diversity_print, '#00C800', 340, 150)
f4 = button_creation('Booking', booking, '#1EBCAD', 40, 350)
f5 = button_creation('Accomodation', accommodation, '#1EBCAD', 640, 350)
f6 = button_creation('Food', FOODS, '#1EBCAD', 340, 550)
f7 = button_creation('Shopping', Shopping, '#DA70D6', 640, 550)
f8 = button_creation('Transportation', facilities, '#DA70D6', 340, 350)
f9 = button_creation('Places To Visit', places, '#DA70D6', 940, 150)
f10 = button_creation('Rating', rating, 'coral', 940, 350)
f11 = button_creation('Health Aid', healthaid, 'coral', 40, 150)
f12 = button_creation('Events', events, 'coral', 40, 550)

main.mainloop()
