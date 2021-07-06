# Demi-Leigh Jefferies Class 1
# Designing a program that allows users to login online
import mysql.connector
from tkinter import *

# Creating the window

window = Tk()
window.title("LOGIN")
window.geometry("800x400")
window.config(bg="gray")
window.resizable(0, 0)

# Creating main screen to either register or login
# Adding an image on top
img = PhotoImage(file="Hnet.com-image.png")
pic = Label(window, image=img, height=110, bg="gray")
pic.photo = img
pic.place(x=236, y=10)

# Adding labels and entries for main screen to enter details

name_lbl = Label(window, fg="white", bg="gray", text="USERNAME: ")
name_lbl.place(x=240, y=170)

id_lbl = Label(window, fg="white", bg="gray", text="ID NUMBER: ")
id_lbl.place(x=240, y=230)

name_ent = Entry(window, fg="green", width=25)
name_ent.place(x=380, y=170)

id_ent = Entry(window, fg="green", width=25)
id_ent.place(x=380, y=230)

# Adding Login, Register and Admin buttons

signIn_btn = Button(window, text="SIGN IN", relief="raised", borderwidth=4, bg="white", width=10, height=1,)
signIn_btn.place(x=70, y=330)

signOut_btn = Button(window, text="SIGN OUT", relief="raised", borderwidth=4, bg="white", width=10, height=1,)
signOut_btn.place(x=250, y=330)

register_btn = Button(window, text="REGISTER", relief="raised", borderwidth=4, bg="white", width=10, height=1,)
register_btn.place(x=430, y=330)

admin_btn = Button(window, text="ADMIN", relief="raised", borderwidth=4, bg="white", width=10, height=1,)
admin_btn.place(x=610, y=330)




window.mainloop()

