# imports
from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk
import wikipediaapi
import requests

translate_image = None
# Translator


def create_translator():
    root = Toplevel(main)
    root.title('Translator')
    root.geometry('910x400')

    # Image button to translate
    translate_image = PhotoImage(file='images\google_translation.png')

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
    image = Label(root, image=translate_image)

    # Window application of data
    input_text.place(x=10, y=130, width=370, height=200)
    input_textbox.place(x=15, y=135, width=360, height=190)
    language_box_i.place(x=130, y=100)

    output_text.place(x=530, y=130, width=370, height=200)
    output_textbox.place(x=535, y=135, width=360, height=190)
    language_box_o.place(x=650, y=100)

    translate_button.place(x=400, y=200)
    # canvas = Canvas(root, width=150, height=150)
    # canvas.place(x=385, y=10)
    # canvas.create_image(0, 0, anchor=NW, image=translate_image)
    # image.pack()


def history_print():
    # Create main window
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
    # Create and place widgets
    label = Label(root, text="Select City", fg='#FF00FF', font=("Arial", 15))
    label.pack(pady=10)

    cities = ['Bangalore', 'Chennai', 'Delhi', 'Kochi', 'Kolkata']
    entry = ttk.Combobox(root, values=cities, state='readonly')
    entry.pack(pady=10)

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


# Main window
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

f1 = Button(main, text='Translator', command=create_translator, width=20, height=5,
            font=("Helvetica", 16, 'bold italic'), relief=FLAT)  # f1 = Translator
f2 = Button(main, text='History', command=history_print, width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT)  # f2 = History
f3 = Button(main, text='Diversity', command=diversity_print, width=20, height=5, font=(
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
    "Helvetica", 16, 'bold italic'), relief=FLAT)  # f8 = Transportation
f9 = Button(main, text='Places To Visit', width=20, height=5, font=(
    "Helvetica", 16, 'bold italic'), relief=FLAT)  # f9 = Places to Visit
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
