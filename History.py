import wikipedia
import requests
from tkinter import *
from tkinter import messagebox, ttk


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
                    history_print.delete(1.0, END)
                    history_print.insert(END, history_text)
                else:
                    messagebox.showinfo("History Section", 'No history found')
            else:
                messagebox.showinfo("History Section", 'No history found')
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Disambiguation error: {e.options}")

    # Create and place widgets
    label = Label(root, text="Enter City:")
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

    history_print = Text(root, bg='white', wrap=WORD, relief=FLAT)
    history_print.pack(pady=10)

    root.mainloop()
