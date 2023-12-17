from tkinter import *
from PIL import Image, ImageTk

def Shopping():
    # Expanded dictionary containing shopping places for different cities
    shopping_places = {
        'Bangalore': [
            'UB City', 'Commercial Street', 'Phoenix Marketcity',
            'Orion Mall', 'Mantri Square Mall', 'Brigade Road',
            'Garuda Mall', 'Forum Mall', 'Gopalan Mall',
            'VR Bengaluru'
        ],
        'Delhi': [
            'Connaught Place', 'Chandni Chowk', 'Select Citywalk',
            'Dilli Haat', 'Pacific Mall', 'Ambience Mall',
            'DLF Promenade', 'Janpath Market', 'Sarojini Nagar Market',
            'Khan Market'
        ],
        'Kolkata': [
            'South City Mall', 'New Market', 'Quest Mall',
            'City Centre Salt Lake', 'Acropolis Mall', 'Mani Square Mall',
            'Metropolis Mall', 'Diamond Plaza', 'Forum Courtyard',
            'Treasure Island Mall'
        ],
        'Kochi': [
            'LuLu Mall', 'Centre Square Mall', 'Oberon Mall',
            'Gold Souk Grande', 'Abad Nucleus Mall', 'Bay Pride Mall',
            'Oberon Mall', 'Centre Square Mall', 'Nucleus Mall',
            'Oberon Mall'
        ],
        'Chennai': [
            'Express Avenue Mall', 'Phoenix Market City', 'Forum Vijaya Mall',
            'Spencer Plaza', 'Grand Mall', 'Ampa Skywalk',
            'VR Chennai', 'Abirami Mega Mall', 'The Marina Mall',
            'Chennai Citi Centre'
        ]
    }

    # Function to display shopping places for the selected city
    def show_shopping_places(city):
        places = shopping_places.get(city, [])
        places_str.set("\n".join(places))

    # Create the main window
    root = Tk()
    root.geometry("500x500")
    root.configure(bg="black")
    root.title("Shopping Places")

    # Load and display an image
    image_path = "shop.jpg"  # Replace with your image file path
    image = Image.open(image_path)
    image = image.resize((300, 200))  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)

    image_label = Label(root, image=photo)
    image_label.image = photo  # To prevent garbage collection
    image_label.pack()

    # Create buttons for each city
    buttons_frame = Frame(root)
    buttons_frame.pack()

    for city in shopping_places.keys():
        city_button = Button(buttons_frame, bg="black", fg="yellow", text=city, command=lambda c=city: show_shopping_places(c))
        city_button.pack(side=LEFT)

    # Variable to hold the shopping places information
    places_str = StringVar()
    places_label = Label(root, bg="black", fg="white", textvariable=places_str)
    places_label.pack()

    root.mainloop()

# Calling the Shopping function
Shopping()
