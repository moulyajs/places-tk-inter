from tkinter import *
from tkinter import messagebox
import csv
from PIL import Image, ImageTk

def accommodation():
    def display_results(image_path=None):
        if image_path:
            display_hotel_image(image_path)
            label.configure(image=photo)
            label.image = photo

    def display_hotel_image(image_path):
        global photo
        window_width = root.winfo_width()  # Get the width of the main window
        window_height = root.winfo_height()  # Get the height of the main window

        img = Image.open(image_path)
        img = img.resize((window_width, window_height))  # Resize the image to match the window size
        new_photo = ImageTk.PhotoImage(img)
        photo = new_photo


    def search_city(keyword, file_name, city_name):
        found = False
        result_text.delete(1.0, END)  # Clear previous results

        with open(file_name, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            if keyword.strip() == "":
                found = True
                for row in reader:
                    result_text.insert(END, f"Hotel name: {row[0]}\n")
            else:
                for row in reader:
                    if keyword.lower() in row[0].lower():
                        found = True
                        result_text.insert(END, f"Hotel name: {row[0]}\n")
                        result_text.insert(END, f"Amenities: {row[1]}\n")
                        result_text.insert(END, f"Price: {row[2]}\n")
                        result_text.insert(END, f"Ratings: {row[3]}\n")
                        display_results(row[4])

                if not found:
                    result_text.insert(END, f"The hotel given is not found in {city_name}\n")

    def on_button_click(city):
        user_input = entry.get()
        if city.lower() == "bangalore":
            search_city(user_input, 'Bangalore.csv', 'Bangalore')
        elif city.lower() == "chennai":
            search_city(user_input, 'Chennai.csv', 'Chennai')
        elif city.lower() == "kolkata":
            search_city(user_input, 'Kolkata.csv', 'Kolkata')
        elif city.lower() == "kochi":
            search_city(user_input, 'Kochi.csv', 'Kochi')
        elif city.lower() == "delhi":
            search_city(user_input, 'Delhi.csv', 'Delhi')
        else:
            messagebox.showerror("Error", "Invalid city selection!")

    root = Tk()
    root.configure(bg='#f2f2f2')
    root.geometry('1000x500')
    root.title("Hotel Search")
    root.configure(bg="#f2f2f2")

    entry = Entry(root, bg="white", fg="black", bd=2)
    entry.pack(pady=10)

    cities = ["Bangalore", "Chennai", "Kolkata", "Kochi", "Delhi"]
    city_frame = Frame(root, bg="#f2f2f2")  # Frame to hold city buttons
    city_frame.pack()

    for city_name in cities:
        button = Button(city_frame, bg="#FFD700", fg="#4B0082", text=city_name, command=lambda c=city_name: on_button_click(c))
        button.pack(side=LEFT, padx=10, pady=10)

    result_text = Text(root, bg="beige", fg="black", height=10, width=50)
    result_text.pack(pady=20)

    label = Label(root)
    label.pack()

    root.mainloop()

# Call the accommodation function to run the GUI
accommodation()
