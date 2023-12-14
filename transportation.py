import tkinter as tk
from datetime import datetime


def check_availability():
    vehicle_type = transport_options.get()
    availability = transportation_data.get(vehicle_type, "Vehicle not found")

    if availability == "Available":
        # Get current date and time
        current_date_time = datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")
        result_label.config(
            text=f"{vehicle_type} is available!\nChecked at: {current_date_time}")
    else:
        result_label.config(text=f"{vehicle_type} is not available.")


def book_transportation():
    vehicle_type = transport_options.get()
    availability = transportation_data.get(vehicle_type, "Vehicle not found")

    if availability == "Available":
        # Get current date and time
        current_date_time = datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")
        result_label.config(
            text=f"Booking {vehicle_type} at: {current_date_time}")
    else:
        result_label.config(
            text=f"{vehicle_type} is not available for booking.")


# Sample transportation data
transportation_data = {"Flight": "Available",
                       "Car": "Available", "Bus": "Not Available"}

# GUI setup
root = tk.Tk()
root.title("Transportation Booking and Availability")

# Widgets
label = tk.Label(root, text="Select Transportation:")
label.pack()

transport_options = tk.StringVar()
transport_options.set("Flight")  # Default option
options_menu = tk.OptionMenu(
    root, transport_options, *transportation_data.keys())
options_menu.pack()

check_button = tk.Button(root, text="Check Availability",
                         command=check_availability)
check_button.pack()

book_button = tk.Button(root, text="Book Transportation",
                        command=book_transportation)
book_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
