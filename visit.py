from tkinter import *


root = Tk()
root.title('Places to visit')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

img = PhotoImage(file='images/bangalore.png')
Label(root, image=img, border=0, bg='white').place(x=20, y=40)
Button(root, width=10, pady=7, text='Bangalore',
       bg='#57a1f8', fg='white', border=0).place(x=45, y=230)
##
img1 = PhotoImage(file='images/chennai.png')
Label(root, image=img1, border=0, bg='white').place(x=600, y=50)
Button(root, width=10, pady=7, text='Chennai',
       bg='#57a1f8', fg='white', border=0).place(x=650, y=230)
##
img2 = PhotoImage(file='images/delhi.png')
Label(root, image=img2, border=0, bg='white').place(x=200, y=50)
Button(root, width=10, pady=7, text='Delhi',
       bg='#57a1f8', fg='white', border=0).place(x=220, y=230)
##
img3 = PhotoImage(file='images/kochi.png')
Label(root, image=img3, border=0, bg='white').place(x=400, y=50)
Button(root, width=10, pady=7, text='Kochi',
       bg='#57a1f8', fg='white', border=0).place(x=450, y=230)
##

# img4 = PhotoImage(file='images/kolkata.jpg')
# Label(root, image=img4, border=0, bg='white').place(x=400, y=200)
# Button(root, width=10, pady=7, text='Kochi',
# bg='#57a1f8', fg='white', border=0).place(x=450, y=230)


root.mainloop()