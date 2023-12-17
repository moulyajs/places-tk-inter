from tkinter import *


def places():
    def display_information(city):
        details_text.config(state=NORMAL)
        details_text.delete(1.0, END)

        if city == 'Bangalore':
            details = "Monuments: Vidhana Soudha, Bangalore Palace, Tipu Sultan's Summer Palace\n"
            details += "Gardens: Lalbagh Botanical Garden, Cubbon Park, Bannerghatta National Park\n"
            details += "Other Places: Bangalore Fort, Nandi Hills"
        elif city == 'Chennai':
            details = "Monuments: Kapaleeshwarar Temple, Fort St. George, Valluvar Kottam\n"
            details += "Gardens: Semmozhi Poonga, Guindy National Park, Arignar Anna Zoological Park\n"
            details += "Other Places: Marina Beach, Government Museum"
        elif city == 'Delhi':
            details = "Monuments: India Gate, Qutub Minar, Humayun's Tomb\n"
            details += "Gardens: Lodhi Gardens, Mughal Gardens, Nehru Park\n"
            details += "Other Places: Red Fort, Akshardham Temple"
        elif city == 'Kochi':
            details = "Monuments: Mattancherry Palace, Fort Kochi, Paradesi Synagogue\n"
            details += "Gardens: Subhash Park, Changampuzha Park, Hill Palace\n"
            details += "Other Places: Fort Kochi Beach, Chinese Fishing Nets"
        elif city == 'Kolkata':
            details = "Monuments: Victoria Memorial, Howrah Bridge, Indian Museum\n"
            details += "Gardens: Maidan, Eden Gardens, Millennium Park\n"
            details += "Other Places: Dakshineswar Kali Temple, Marble Palace"
        else:
            details = "Details not available for this city."

        details_text.insert(END, f"Places to visit in  {city}:\n\n{details}")
        details_text.config(state=DISABLED)

    root = Toplevel()
    root.title('Places to visit')
    root.geometry('925x700+300+200')
    root.configure(bg='#fff')
    root.resizable(True, True)

    img = PhotoImage(file='images/bangalorepic.png')
    label_bangalore = Label(root, image=img, border=0, bg='white')
    label_bangalore.place(x=20, y=40)
    label_bangalore_info = Label(root, width=30, pady=7, text='Bangalore',
                                 bg='#57a1f8', fg='white', border=0)
    label_bangalore_info.place(x=130, y=350)
    label_bangalore_info.bind(
        "<Button-1>", lambda event: display_information('Bangalore'))

    img1 = PhotoImage(file='images/chennaipic.png')
    label_chennai = Label(root, image=img1, border=0, bg='white')
    label_chennai.place(x=450, y=40)
    label_chennai_info = Label(root, width=30, pady=7, text='Chennai',
                               bg='#57a1f8', fg='white', border=0)
    label_chennai_info.place(x=550, y=350)
    label_chennai_info.bind(
        "<Button-1>", lambda event: display_information('Chennai'))

    img2 = PhotoImage(file='images/delhipic.png')
    label_delhi = Label(root, image=img2, border=0, bg='white')
    label_delhi.place(x=900, y=40)
    label_delhi_info = Label(root, width=30, pady=7, text='Delhi',
                             bg='#57a1f8', fg='white', border=0)
    label_delhi_info.place(x=950, y=350)
    label_delhi_info.bind(
        "<Button-1>", lambda event: display_information('Delhi'))

    img3 = PhotoImage(file='images/kochipic.png')
    label_kochi = Label(root, image=img3, border=0, bg='white')
    label_kochi.place(x=20, y=450)
    label_kochi_info = Label(root, width=30, pady=7, text='Kochi',
                             bg='#57a1f8', fg='white', border=0)
    label_kochi_info.place(x=30, y=670)
    label_kochi_info.bind(
        "<Button-1>", lambda event: display_information('Kochi'))

    img4 = PhotoImage(file='images/kolkatapic.png')
    label_kolkata = Label(root, image=img4, border=0, bg='white')
    label_kolkata.place(x=450, y=450)
    label_kolkata_info = Label(root, width=30, pady=7, text='Kolkata',
                               bg='#57a1f8', fg='white', border=0)
    label_kolkata_info.place(x=500, y=670)
    label_kolkata_info.bind(
        "<Button-1>", lambda event: display_information('Kolkata'))

    # Information label at the bottom right
    details_text = Text(root, wrap=WORD, width=40, height=10,
                        state=DISABLED, bg='#57a1f8', font=("Arial", 12), padx=10, pady=10)
    details_text.place(relx=0.9, rely=0.9, anchor='se')

    root.mainloop()


if __name__ == "__main__":
    places()
