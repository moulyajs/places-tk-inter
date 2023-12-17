from tkinter import *
from tkinter import ttk,messagebox

def diversity_print():
    # Create main window
    root = Tk()
    root.title("City Information")

    # Create and place widgets
    label = Label(root, text="Select City", fg='#FF00FF', font=("Arial", 15))
    label.pack(pady=10)

    cities = ['Bangalore', 'Chennai', 'Delhi', 'Kochi', 'Kolkata']
    combo = ttk.Combobox(root, values=cities, state='readonly')
    combo.pack(pady=10)
    combo.set('City')  # Set the default value

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

    text_display = Text(root, bg='white', fg='blue', wrap=WORD, relief=FLAT, height=20, width=90)
    text_display.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()