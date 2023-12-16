from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

main_window = Tk()
main_window.title("Voyageur")
main_window.geometry("300x300")


def create_translator():
    # Page details
    root = Toplevel(main_window)
    root.title('Translator')
    root.geometry('910x400')

    # Image button to translate
    icon = PhotoImage(
        file=r'C:\Users\nandi\Desktop\Python\Voyageur\Microsoft_Translator_Logo.png')

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

    # Translator
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
    image = Label(root, image=icon, relief=FLAT)

    input_text = Frame(root, bd=5, bg='sky blue')
    input_textbox = Text(root, bg='white', wrap=WORD,
                         relief=FLAT)  # Take input to translate
    input_scrollbar = Scrollbar(input_textbox)
    input_textbox.configure(yscrollcommand=input_scrollbar.set)

    output_text = Frame(root, bd=5, bg='sky blue')
    output_textbox = Text(root, bg='white', wrap=WORD,
                          relief=FLAT)  # To display the translation
    output_scrollbar = Scrollbar(output_textbox)
    output_textbox.configure(yscrollcommand=input_scrollbar.set)

    translate_button = Button(root, image=icon, command=trans, relief=FLAT)

    # Window application of data
    # image.place(x = 390,y = 10)

    input_text.place(x=10, y=130, width=370, height=200)
    input_textbox.place(x=15, y=135, width=360, height=190)
    language_box_i.place(x=130, y=100)

    output_text.place(x=530, y=130, width=370, height=200)
    output_textbox.place(x=535, y=135, width=360, height=193900)
    language_box_o.place(x=650, y=100)

    translate_button.place(x=390, y=170)


translation_button = Button(
    main_window, text='Translator', command=create_translator)
translation_button.pack()
main_window.mainloop()
