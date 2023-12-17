import csv
from tkinter import Tk, Label, Button, Frame

def create_window(title, function):
    root = Tk()
    root.title(title + " Portal")
    root.geometry('500x500')

    # Header
    header_label = Label(root, text=f'{title} Window', font=50)
    header_label.pack()

    # Frame
    frame = Frame(root)
    frame.pack()

    # Bottom Frame
    bottom_frame = Frame(root)
    bottom_frame.pack(side='BOTTOM')

    # Buttons
    cities = ['Bangalore', 'Delhi', 'Chennai', 'Kolkata', 'Kochi']
    buttons = [Button(frame, text=city, command=lambda c=city: function(c)) for city in cities]

    for button in buttons:
        button.pack()

    # Output Label
    output_label = Label(root, text="")
    output_label.pack()

    root.mainloop()

def show_output(data):
    text = "\n".join(data)
    output_label.config(text=text)

def booking():
    def booking2(city):
        n = []
        with open('booking.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[1] == city:
                    n.append(row[0] + ":" + row[2])
        show_output(n)

    create_window("Booking", booking2)

def rating():
    def rating2(city):
        n = []
        with open('rate.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == city:
                    n.append(row[1])
        show_output(n)

    create_window("Rating", rating2)

def healthaid():
    def healthaid2(city):
        n = []
        with open('healthaid.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == city:
                    n.append(row[1])
        show_output(n)

    create_window("HealthAid", healthaid2)

def events():
    def events2(city):
        n = []
        with open('events.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == city:
                    n.append(row[1] + ":" + row[2] + "," + row[3])
        show_output(n)

    create_window("Events", events2)

# Run the desired function
booking()
# rating()
# healthaid()
# events()
