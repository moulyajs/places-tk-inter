import tkinter as tk
from tkinter import ttk


def display_date():
    date = date_entry.get()
    date_label.config(text=f"Date: {date}")


def display_from_location():
    from_location = from_location_entry.get()
    from_location_label.config(text=f"From Location: {from_location}")


def display_to_location():
    to_location = to_location_entry.get()
    to_location_label.config(text=f"To Location: {to_location}")


def display_transportation():
    selected_transport = transportation_combobox.get()
    available_times = get_available_times(selected_transport)
    time_label.config(
        text=f"Transportation Facility: {selected_transport}\nAvailable Times: {', '.join(available_times)}")


def get_available_times(transport):
    # Replace this with your logic to get actual available times based on the selected transportation
    if transport == "Car":
        return ["8:00 AM", "12:00 PM", "3:00 PM"]
    elif transport == "Bus":
        return ["9:00 AM", "1:00 PM", "4:00 PM"]
    elif transport == "Train":
        return ["10:00 AM", "2:00 PM", "5:00 PM"]
    elif transport == "Flight":
        return ["7:00 AM", "11:00 AM", "2:30 PM", "6:00 PM"]


# Create main window
root = tk.Tk()
root.title("Transportation Details")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(True, True)
# Date Entry
date_label = tk.Label(root, text="Enter Date:", font=('Helvetica', 11))
date_label.place(x=350, y=100)

date_entry = tk.Entry(root, bg='lightgrey', width=28, font=('Helvetica', 11))
date_entry.place(x=500, y=100)

date_button = tk.Button(root, text="Enter Date",
                        bg='#4681f4', fg='white', font=('Helvetica', 11), command=display_date)
date_button.place(x=800, y=100)

# From Location Entry
from_location_label = tk.Label(
    root, text="Enter From Location:", font=('Helvetica', 11))
from_location_label.place(x=350, y=150)

from_location_entry = tk.Entry(
    root, bg='lightgrey', width=28, font=('Helvetica', 11))
from_location_entry.place(x=500, y=150)

from_location_button = tk.Button(
    root, text="Enter From Location", bg='#4681f4', fg='white', font=('Helvetica', 11), command=display_from_location)
from_location_button.place(x=800, y=150)

# To Location Entry
to_location_label = tk.Label(
    root, text="Enter To Location:", font=('Helvetica', 11))
to_location_label.place(x=350, y=200)

to_location_entry = tk.Entry(
    root, bg='lightgrey', width=28, font=('Helvetica', 11))
to_location_entry.place(x=500, y=200)

to_location_button = tk.Button(
    root, text="Enter To Location", bg='#4681f4', fg='white',  font=('Helvetica', 11), command=display_to_location)
to_location_button.place(x=800, y=200)

# Transportation Facilities

transportation_label = tk.Label(root,  font=(
    'Helvetica', 11), text="Select Transportation:")
transportation_label.place(x=350, y=250)

transportation_options = ["Car", "Bus", "Train", "Flight"]
transportation_combobox = ttk.Combobox(
    root, width=28,  values=transportation_options, font=('Helvetica', 11))
transportation_combobox.place(x=500, y=250)
transportation_button = tk.Button(
    root, text="Get Transportation", bg='#4681f4', fg='white', font=('Helvetica', 11), command=display_transportation)
transportation_button.place(x=800, y=250)

# Display Time
time_label = tk.Label(root, text="", bg='#55c2da',
                      fg='black', font=('Helvetica', 11))
time_label.place(x=450, y=300)

# Run the Tkinter event loop
root.mainloop()
