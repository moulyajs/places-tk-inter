from tkinter import *
from tkinter import messagebox


def show_places(selected_place):
    if selected_place == "Bangalore":
        display_places(["Monument 1", "Monument 2", "Garden 1", "Garden 2"])
    elif selected_place == "Chennai":
        display_places(["Monument A", "Monument B", "Garden X", "Garden Y"])
    elif selected_place == "Delhi":
        display_places(["India Gate", "Qutub Minar",
                       "Lodhi Garden", "Hauz Khas"])
    elif selected_place == "Kochi":
        display_places(["Fort Kochi", "Jewish Synagogue",
                       "Hill Palace", "Marine Drive"])
    elif selected_place == "Kolkata":
        display_places(["Victoria Memorial", "Howrah Bridge",
                       "Botanical Garden", "Eden Gardens"])
    else:
        messagebox.showinfo("Error", "Invalid selection")


def display_places(places):
    result = "\n".join(places)
    messagebox.showinfo("Places in the City", f"Places to visit:\n{result}")


root = Tk()
root.title('Places to visit')
root.geometry('1200x800+300+200')
root.configure(bg='#fff')
root.resizable(True, True)

img = PhotoImage(file='images/bangalore.png')
Label(root, image=img, border=0, bg='white').place(x=20, y=40)
Button(root, width=30, pady=7, text='Bangalore',
       bg='#57a1f8', fg='white', border=0, command=lambda: show_places("Bangalore")).place(x=130, y=350)

img1 = PhotoImage(file='images/chennai.png')
Label(root, image=img1, border=0, bg='white').place(x=450, y=40)
Button(root, width=30, pady=7, text='Chennai',
       bg='#57a1f8', fg='white', border=0, command=lambda: show_places("Chennai")).place(x=550, y=350)

img2 = PhotoImage(file='images/delhi.png')
Label(root, image=img2, border=0, bg='white').place(x=900, y=40)
Button(root, width=30, pady=7, text='Delhi',
       bg='#57a1f8', fg='white', border=0, command=lambda: show_places("Delhi")).place(x=950, y=350)

img3 = PhotoImage(file='images/kochi.png')
Label(root, image=img3, border=0, bg='white').place(x=20, y=450)
Button(root, width=30, pady=7, text='Kochi',
       bg='#57a1f8', fg='white', border=0, command=lambda: show_places("Kochi")).place(x=30, y=670)

img4 = PhotoImage(file='images/kolkata.png')
Label(root, image=img4, border=0, bg='white').place(x=450, y=450)
Button(root, width=30, pady=7, text='Kolkata',
       bg='#57a1f8', fg='white', border=0, command=lambda: show_places("Kolkata")).place(x=500, y=670)

root.mainloop()
