import tkinter
import csv
from tkinter import *


def booking():
    n = []

    def booking2(l):
        f = open('booking.csv', 'r')
        r = csv.reader(f)
        for i in r:
            if i[1] == l:
                n.append(i[0]+":"+i[2])
        show_output(n)

    def show_output(a):
        text = "\n".join(a)
        # Function to display output
        output_label.config(text=text)
    root = tkinter.Tk()
    root.title("Booking Portal")
    root.geometry('500x500')
    w = Label(root, text='Booking Window', font=50)
    w.pack()
    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)
    b1 = Button(frame, text="Banglore", command=lambda: booking2('Bangalore'))
    b1.pack()
    b2 = Button(frame, text="Delhi", command=lambda: booking2('Delhi'))
    b2.pack()
    b3 = Button(frame, text="Chennai", command=lambda: booking2('Chennai'))
    b3.pack()
    b4 = Button(frame, text="Kolkata", command=lambda: booking2('Kolkata'))
    b4.pack()
    b5 = Button(frame, text="Kochi", command=lambda: booking2('Kochi'))
    b5.pack()
    output_label = tkinter.Label(root, text="")
    output_label.pack()
    root.mainloop()


def rating():
    n = []

    def rating2(l):
        f = open('rate.csv', 'r')
        r = csv.reader(f)
        print("The various rating provided for", l, "are")
        for i in r:
            if i[0] == l:
                n.append(i[1])
        show_output(n)

    def show_output(a):
        text = "\n".join(a)
        # Function to display output
        output_label.config(text=text)
    root = tkinter.Tk()
    root.title("Rating Portal")
    root.geometry('500x500')
    w = Label(root, text='Rating Window', font=50)
    w.pack()
    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)
    b1 = Button(frame, text="Banglore", command=lambda: rating2('Bangalore'))
    b1.pack()
    b2 = Button(frame, text="Delhi", command=lambda: rating2('Delhi'))
    b2.pack()
    b3 = Button(frame, text="Chennai", command=lambda: rating2('Chennai'))
    b3.pack()
    b4 = Button(frame, text="Kolkata", command=lambda: rating2('Kolkata'))
    b4.pack()
    b5 = Button(frame, text="Kochi", command=lambda: rating2('Kochi'))
    b5.pack()
    output_label = tkinter.Label(root, text="")
    output_label.pack()
    root.mainloop()


def healthaid():
    n = []

    def healthaid2(l):
        f = open('healthaid.csv', 'r')
        r = csv.reader(f)
        print("The various hospitals are")
        for i in r:
            if i[0] == l:
                n.append(i[1])
        show_output(n)

    def show_output(a):
        text = "\n".join(a)
        # Function to display output
        output_label.config(text=text)
    root = tkinter.Tk()
    root.title("HealthAid Portal")
    root.geometry('500x500')
    w = Label(root, text='HealthAid Window', font=50)
    w.pack()
    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)
    b1 = Button(frame, text="Banglore",
                command=lambda: healthaid2('Bangalore'))
    b1.pack()
    b2 = Button(frame, text="Delhi", command=lambda: healthaid2('Delhi'))
    b2.pack()
    b3 = Button(frame, text="Chennai", command=lambda: healthaid2('Chennai'))
    b3.pack()
    b4 = Button(frame, text="Kolkata", command=lambda: healthaid2('Kolkata'))
    b4.pack()
    b5 = Button(frame, text="Kochi", command=lambda: healthaid2('Kochi'))
    b5.pack()
    output_label = tkinter.Label(root, text="")
    output_label.pack()
    root.mainloop()


def events():
    n = []

    def events2(l):
        f = open('events.csv', 'r')
        r = csv.reader(f)
        print("The various events are:")
        for i in r:
            if i[0] == l:
                n.append(i[1]+":"+i[2]+","+i[3])
        show_output(n)

    def show_output(a):
        text = "\n".split()
        # Function to display output
        output_label.config(text=text)
    root = tkinter.Tk()
    root.title("Events Portal")
    root.geometry('500x500')
    w = Label(root, text='Events Window', font=50)
    w.pack()
    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)
    b1 = Button(frame, text="Banglore", command=lambda: events2('Bangalore'))
    b1.pack()
    b2 = Button(frame, text="Delhi", command=lambda: events2('Delhi'))
    b2.pack()
    b3 = Button(frame, text="Chennai", command=lambda: events2('Chennai'))
    b3.pack()
    b4 = Button(frame, text="Kolkata", command=lambda: events2('Kolkata'))
    b4.pack()
    b5 = Button(frame, text="Kochi", command=lambda: events2('Kochi'))
    b5.pack()
    output_label = tkinter.Label(root, text="")
    output_label.pack()
    root.mainloop()


if __name__ == "__main__":
    healthaid()
    rating()
    booking()
