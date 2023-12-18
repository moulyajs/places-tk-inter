# imports
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk
import wikipedia
import requests
import csv

# Translator


def create_translator():
    root = Toplevel()
    root.title('Translator')
    root.geometry('910x400')

    # Image button to translate
    img = Image.open(r'images\google_translation.jpg')
    img = img.resize((30, 30))
    translate_image = ImageTk.PhotoImage(img)

    # Create list of languages
    languages = LANGUAGES.items()
    list_of_languages_o = [(f"{language.upper()}({code})")
                           for code, language in languages]
    list_of_languages_i = [(f"{language.upper()}({code})")
                           for code, language in languages]

    # Dropbox of languages
    # to translate to which language
    language_box_o = ttk.Combobox(
        root, values=list_of_languages_o, state='readonly')
    # Default statement present in dropbox
    language_box_o.set('Select Language')

    # to input in which language
    language_box_i = ttk.Combobox(
        root, values=list_of_languages_i, state='readonly')
    language_box_i.set('ENGLISH(en)')  # Default statement present in dropbox

    # Get which language entered
    def get_lang(x):
        a = x.split('(')
        code = a[1]
        code = code[:len(a[1]) - 1]
        return code

    # Translation
    def trans():
        translate = Translator()
        text = input_textbox.get(1.0, END)
        try:
            input_language = get_lang(language_box_i.get())
            output_language = get_lang(language_box_o.get())

            translation = translate.translate(
                text, src=input_language, dest=output_language)
            output_textbox.delete(1.0, END)
            output_textbox.insert(END, translation.text)
        except Exception:
            messagebox.showinfo('Error', 'Please enter text to translate')

    # Input for translation
    input_text = Frame(root, bd=5, bg='sky blue')
    input_textbox = Text(root, bg='white', wrap=WORD,
                         relief=FLAT)  # Take input to translate
    input_scrollbar = Scrollbar(input_textbox)
    input_textbox.configure(yscrollcommand=input_scrollbar.set)

    output_text = Frame(root, bd=5, bg='sky blue')
    output_textbox = Text(root, bg='white', wrap=WORD,
                          relief=FLAT)  # To display the translation
    output_scrollbar = Scrollbar(output_textbox)
    output_textbox.configure(yscrollcommand=output_scrollbar.set)

    # translate_button = Button(root, image = translate_image, command=trans, relief=FLAT)
    translate_button = Button(root, text='TRANSLATE', command=trans, relief=FLAT, font=(
        "Arial Narrow", 16), fg='blue')
    print_image = Label(root, image=translate_image)

    # Window application of data
    input_text.place(x=10, y=130, width=370, height=200)
    input_textbox.place(x=15, y=135, width=360, height=190)
    language_box_i.place(x=130, y=100)

    output_text.place(x=530, y=130, width=370, height=200)
    output_textbox.place(x=535, y=135, width=360, height=190)
    language_box_o.place(x=650, y=100)

    translate_button.place(x=400, y=200)
    print_image.place(x=400, y=90)


def history_print():
    root = Tk()
    root.title("History")

    def get_headings(page_name):
        headers = {'User-Agent': 'YourUserAgent/1.0'}
        url = f'https://en.wikipedia.org/w/api.php?action=parse&format=json&page={page_name}'
        url_request = requests.get(url, headers=headers)
        data = url_request.json()
        if 'parse' in data and 'sections' in data['parse']:
            return [section['anchor'] for section in data['parse']['sections'] if section['toclevel'] == 1]

    def history_data(page_name):
        headings = get_headings(page_name)
        try:
            # Get the first suggestion without asking the user
            suggestions = wikipedia.search(page_name, results=1)
            if suggestions:
                page = wikipedia.page(suggestions[0], auto_suggest=False)
                content = page.content
            # Find the start and end indices of the "History" section
                start = content.find("History")
                end = content.find(headings[headings.index(
                    "History") + 1]) if 'History' in headings and headings.index('History') + 1 < len(headings) else None
                if start != -1 and end:
                    history_text = content[start-3:end-3]
                    printing_history.delete(1.0, END)
                    printing_history.insert(END, history_text)
                else:
                    messagebox.showinfo("History Section", 'No history found')
            else:
                messagebox.showinfo("History Section", 'No history found')
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Disambiguation error: {e.options}")

    label = Label(root, text="Select City", fg='#FF00FF', font=("Arial", 15))
    label.pack(pady=10)

    cities = ['Bangalore', 'Chennai', 'Delhi', 'Kochi', 'Kolkata']
    entry = ttk.Combobox(root, values=cities, state='readonly')
    entry.pack(pady=10)
    entry.set('City')  # default value

    def on_button_click():
        page_name = entry.get()
        page_name = page_name.capitalize()
        history_text = history_data(page_name)

    button = Button(root, text="History", command=on_button_click)
    button.pack(pady=10)

    printing_history = Text(root, bg='white', wrap=WORD, relief=FLAT)
    printing_history.pack(pady=10)


def diversity_print():
    root = Tk()
    root.title("Diversity")

    label = Label(root, text="Select City", fg='#008000', font=("Arial", 15))
    label.pack(pady=10)

    cities = ['Bangalore', 'Chennai', 'Delhi', 'Kochi', 'Kolkata']
    combo = ttk.Combobox(root, values=cities, state='readonly')
    combo.pack(pady=10)
    combo.set('City')  # default value

    def display_content():
        selected_city = combo.get()
        file_name = f'{selected_city}.txt'
        try:
            with open(file_name, 'r', encoding='utf8') as file:
                content = file.read()
                text_display.delete(1.0, END)
                text_display.insert(END, content)
        except FileNotFoundError:
            text_display.delete(1.0, END)
            messagebox.showinfo('SORRY', f'No diversity for {selected_city}')

    button = Button(root, text="Diversity", command=display_content)
    button.pack()

    text_display = Text(root, bg='white', fg='blue',
                        wrap=WORD, relief=FLAT, height=20, width=90)
    text_display.pack(pady=10)


def FOODS():
    def display_foods(city):
        city_foods = {
            "Bangalore": [
                "Masala Dosa", "Idli Vada", "Bisi Bele Bath", "Ragi Mudde", "Mysore Pak",
                "Puliyogare", "Ragi Dosa", "Obbattu/Holige", "Akki Roti", "Kesari Bath"
            ],
            "Kolkata": [
                "Kathi Roll", "Macher Jhol", "Rosogolla", "Phuchka", "Mishti Doi",
                "Chingri Macher Malai Curry", "Sondesh", "Macher Chop", "Aloo Posto"
            ],
            "Delhi": [
                "Chole Bhature", "Butter Chicken", "Aloo Chaat", "Paranthas", "Dahi Bhalla",
                "Kebabs", "Rajma Chawal", "Nihari", "Samosa", "Kulfi"
            ],
            "Kochi": [
                "Appam with Stew", "Malabar Parotta with Kerala Beef Fry", "Karimeen Pollichathu",
                "Puttu and Kadala Curry", "Fish Molee", "Thalassery Biryani", "Kappa and Meen Curry",
                "Erachi Varutharacha Curry", "Idiyappam with Egg Curry", "Ada Pradhaman"
            ],
            "Chennai": [
                "Dosa", "Idli Sambar", "Chettinad Chicken", "Pongal", "Filter Coffee",
                "Masala Vada", "Kothu Parotta", "Upma", "Nelloor Biryani", "Murukku"
            ]
        }

        foods = city_foods.get(city, [])
        food_list = "\n".join(foods)
        display[city]["label"].config(text=food_list)

    root = Toplevel()
    root.title("Best Foods in Cities")
    root.geometry("900x400")  # Adjusted window size for better layout
    root.configure(bg="black")  # Background color

    # Updated city_info with image paths and position for food display
    city_info = {
        "Bangalore": {"position": (0, 0), "image": r"images\blr.jpg.", "food_col": 3},
        "Kolkata": {"position": (0, 1), "image": r"images\kol.jpg", "food_col": 3},
        "Delhi": {"position": (0, 2), "image": r"images\delhi.jpg", "food_col": 3},
        "Kochi": {"position": (0, 3), "image": r"images\kochi.jpeg.jpg", "food_col": 3},
        "Chennai": {"position": (0, 4), "image": r"images\chennai.jpg", "food_col": 3}
    }

    cities = ["Bangalore", "Kolkata", "Delhi", "Kochi", "Chennai"]
    selected_city = StringVar(root)
    selected_city.set("Choose the city")

    def city_button_click(city_name):
        selected_city.set(city_name)
        display_foods(city_name)

    display = {}
    for city in cities:
        info = city_info[city]
        row, col = info["position"]

        # Load and resize images
        img = Image.open(info["image"])
        img = img.resize((100, 100))
        img = ImageTk.PhotoImage(img)

        # Create a label to display the image
        img_label = Label(root, image=img)
        img_label.image = img
        img_label.grid(row=row, column=col)  # Image on top

        # Button for city name
        button = Button(root, text=city, compound=TOP,
                        command=lambda c=city: city_button_click(c))
        button.config(bg="#FFD700", fg="brown", font=(
            "Arial", 10), width=7, height=1)
        button.grid(row=row+1, column=col)  # Button below the image

        # Display label for food items
        food_display = Label(root, text="", justify="right",
                             bg="black", fg='white', font=("Arial", 10))
        # Food items on the side
        food_display.grid(row=info["food_col"], column=col, padx=10, pady=10)

        # Store each city's display label in the dictionary
        display[city] = {"label": food_display}


def booking():
    n = []

    def booking2(l):
        nonlocal n
        n = []  # Clear the data before appending new data
        with open('booking.csv', 'r') as f:
            r = csv.reader(f)

            def show_output(a):
                text = "\n".join(a)
                # Function to display output
                output_label.delete(1.0, END)
                output_label.insert(END, text)

            for i in r:
                if i[1] == l:
                    n.append(i[0] + ":" + i[2])
            show_output(n)

    root = Toplevel()
    root.title("Booking Portal")
    root.geometry('500x550')

    w = Label(root, text='Booking Window', font=50)
    w.pack()

    frame = Frame(root, bg='black', bd=50)
    frame.pack()

    b1 = Button(frame, text="Banglore", fg='white', bg='black',
                command=lambda: booking2('Bangalore'))
    b1.pack()

    b2 = Button(frame, text="Delhi", fg='white', bg='black',
                command=lambda: booking2('Delhi'))
    b2.pack()

    b3 = Button(frame, text="Chennai", fg='white', bg='black',
                command=lambda: booking2('Chennai'))
    b3.pack()

    b4 = Button(frame, text="Kolkata", fg='white', bg='black',
                command=lambda: booking2('Kolkata'))
    b4.pack()

    b5 = Button(frame, text="Kochi", fg='white', bg='black',
                command=lambda: booking2('Kochi'))
    b5.pack()

    output_label = Text(root, wrap=WORD)
    output_label.pack()

    image_path = r"images\bookingimage.jpg"  # Replace with your image path
    img = Image.open(image_path)
    img = img.resize((300, 100), Image.NEAREST)  # Resize the image as needed
    photo = ImageTk.PhotoImage(img)

    image_label = Label(root, image=photo)
    image_label.image = photo  # To prevent image from being garbage collected
    image_label.pack(side=BOTTOM, pady=10)


def rating():
    n = []

    def label_writing():
        # You can use this function to write labels if needed in the future
        pass

    def rating2(l):
        n.clear()  # Clear the list before appending new ratings
        with open('rate.csv', 'r') as f:
            r = csv.reader(f)
            for i in r:
                if i[0] == l:
                    n.append(i[1])
        show_output(n)

    def show_output(a):
        text = "\n".join(a)
        # Use '1.0' instead of 1.0 for Text widget
        output_label.delete('1.0', END)
        output_label.insert(END, text)

    root = Toplevel()
    root.title("Rating Portal")
    root.geometry('500x500')

    w = Label(root, text='Rating Window', font=50)
    w.pack()

    frame = Frame(root, bg='black', bd=50)
    frame.pack()

    b1 = Button(frame, text="Bangalore", fg='white', bg='black',
                command=lambda: rating2('Bangalore'))  # Fixed spelling
    b1.pack()

    b2 = Button(frame, text="Delhi", fg='white', bg='black',
                command=lambda: rating2('Delhi'))
    b2.pack()

    b3 = Button(frame, text="Chennai", fg='white', bg='black',
                command=lambda: rating2('Chennai'))
    b3.pack()

    b4 = Button(frame, text="Kolkata", fg='white', bg='black',
                command=lambda: rating2('Kolkata'))
    b4.pack()

    b5 = Button(frame, text="Kochi", fg='white', bg='black',
                command=lambda: rating2('Kochi'))
    b5.pack()

    # Use 'word' directly instead of WORDS
    output_label = Text(root, wrap='word')
    output_label.pack()

    image_path = r"images\ratingimage.jpg"
    img = Image.open(image_path)
    img = img.resize((300, 100), Image.NEAREST)  # Resize the image as needed
    photo = ImageTk.PhotoImage(img)

    image_label = Label(root, image=photo)
    image_label.image = photo  # To prevent image from being garbage collected
    image_label.pack(side=BOTTOM, pady=10)


def healthaid():
    n = []

    def healthaid2(l):
        nonlocal n
        n = []  # Clear the data before appending new data
        with open('healthaid.csv', 'r') as f:
            r = csv.reader(f)

            def show_output(a):
                text = "\n".join(a)
                # Function to display output
                output_label.delete(1.0, END)
                output_label.insert(END, text)

            for i in r:
                if i[0] == l:
                    n.append(i[1])
            show_output(n)

    root = Toplevel()
    root.title("Healthaid Portal")
    root.geometry('500x500')

    w = Label(root, text='Healthaid Window', font=50)
    w.pack()

    frame = Frame(root, bg='black', bd=50)
    frame.pack()

    b1 = Button(frame, text="Banglore", fg='white', bg='black',
                command=lambda: healthaid2('Bangalore'))
    b1.pack()

    b2 = Button(frame, text="Delhi",  fg='white', bg='black',
                command=lambda: healthaid2('Delhi'))
    b2.pack()

    b3 = Button(frame, text="Chennai", fg='white', bg='black',
                command=lambda: healthaid2('Chennai'))
    b3.pack()

    b4 = Button(frame, text="Kolkata", fg='white', bg='black',
                command=lambda: healthaid2('Kolkata'))
    b4.pack()

    b5 = Button(frame, text="Kochi",  fg='white', bg='black',
                command=lambda: healthaid2('Kochi'))
    b5.pack()

    output_label = Text(root, wrap=WORD)
    output_label.pack()

    image_path = r"images\hospitals.jpg"
    img = Image.open(image_path)
    img = img.resize((300, 100), Image.NEAREST)  # Resize the image as needed
    photo = ImageTk.PhotoImage(img)

    image_label = Label(root, image=photo)
    image_label.image = photo  # To prevent image from being garbage collected
    image_label.pack(side=BOTTOM, pady=10)


def events():
    n = []

    def events2(l):
        nonlocal n
        n = []  # Clear the data before appending new data
        with open('events.csv', 'r') as f:
            r = csv.reader(f)

            def show_output(a):
                text = "\n".join(a)
                # Function to display output
                output_label.delete(1.0, END)
                output_label.insert(END, text)

            for i in r:
                if i[0] == l:
                    n.append(i[1]+":"+i[2]+","+i[3])
            show_output(n)

    root = Toplevel()
    root.title("Events Portal")
    root.geometry('500x500')

    w = Label(root, text='Events Window', font=50)
    w.pack()

    frame = Frame(root, bg='black', bd=50)
    frame.pack()

    b1 = Button(frame, text="Banglore", fg='white', bg='black',
                command=lambda: events2('Bangalore'))
    b1.pack()

    b2 = Button(frame, text="Delhi", fg='white', bg='black',
                command=lambda: events2('Delhi'))
    b2.pack()

    b3 = Button(frame, text="Chennai", fg='white', bg='black',
                command=lambda: events2('Chennai'))
    b3.pack()

    b4 = Button(frame, text="Kolkata",  fg='white',
                bg='black', command=lambda: events2('Kolkata'))
    b4.pack()

    b5 = Button(frame, text="Kochi", fg='white', bg='black',
                command=lambda: events2('Kochi'))
    b5.pack()

    output_label = Text(root, wrap=WORD)
    output_label.pack()

    image_path = r"images\events.jpg"
    img = Image.open(image_path)
    img = img.resize((300, 100), Image.NEAREST)  # Resize the image as needed
    photo = ImageTk.PhotoImage(img)

    image_label = Label(root, image=photo)
    image_label.image = photo  # To prevent image from being garbage collected
    image_label.pack(side=BOTTOM, pady=10)


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
        # Resize the image to match the window size
        img = img.resize((window_width, window_height))
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
                    result_text.insert(
                        END, f"The hotel given is not found in {city_name}\n")

    def on_button_click(city):
        user_input = entry.get()
        try:
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
        except Exception:
            messagebox.showerror("Error", "Invalid city selection!")

    root = Toplevel()
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
        button = Button(city_frame, bg="#FFD700", fg="#4B0082",
                        text=city_name, command=lambda c=city_name: on_button_click(c))
        button.pack(side=LEFT, padx=10, pady=10)

    result_text = Text(root, bg="beige", fg="black", height=10, width=50)
    result_text.pack(pady=20)

    label = Label(root)
    label.pack()


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
    root = Toplevel()
    root.geometry("500x500")
    root.configure(bg="black")
    root.title("Shopping Places")

    # Load and display an image
    image_path = r"images\shop.webp"  # Replace with your image file path
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
        city_button = Button(buttons_frame, bg="black", fg="yellow",
                             text=city, command=lambda c=city: show_shopping_places(c))
        city_button.pack(side=LEFT)

    # Variable to hold the shopping places information
    places_str = StringVar()
    places_label = Label(root, bg="black", fg="white", textvariable=places_str)
    places_label.pack()
