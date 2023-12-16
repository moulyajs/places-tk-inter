from tkinter import *


root = Tk()
root.title('Places to visit')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(True, True)

img = PhotoImage(file='images/bangalore.png')
Label(root, image=img, border=0, bg='white').place(x=20, y=40)
Label(root, width=30, pady=7, text='Bangalore',
      bg='#57a1f8', fg='white', border=0).place(x=130, y=350)

img1 = PhotoImage(file='images/chennai.png')
Label(root, image=img1, border=0, bg='white').place(x=450, y=40)
Label(root, width=30, pady=7, text='Chennai',
      bg='#57a1f8', fg='white', border=0).place(x=550, y=350)

img2 = PhotoImage(file='images/delhi.png')
Label(root, image=img2, border=0, bg='white').place(x=900, y=40)
Label(root, width=30, pady=7, text='Delhi',
      bg='#57a1f8', fg='white', border=0).place(x=950, y=350)

img3 = PhotoImage(file='images/kochi.png')
Label(root, image=img3, border=0, bg='white').place(x=20, y=450)
Label(root, width=30, pady=7, text='Kochi',
      bg='#57a1f8', fg='white', border=0).place(x=30, y=670)
##

img4 = PhotoImage(file='images/kolkata.png')
Label(root, image=img4, border=0, bg='white').place(x=450, y=450)
Label(root, width=30, pady=7, text='Kolkata',
      bg='#57a1f8', fg='white', border=0).place(x=500, y=670)


root.mainloop()
