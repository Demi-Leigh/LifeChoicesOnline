# Demi-Leigh Jefferies Class 1
# Designing a program that allows users to login online
import mysql.connector
from tkinter import *

# Creating the window

window = Tk()
window.title("REGISTER")
window.geometry("700x540")
window.config(bg="gray")
window.resizable(0, 0)

# Creating main screen to either register or login
# Adding an image on top
img = PhotoImage(file="Hnet.com-image.png")
pic = Label(window, image=img, height=110, bg="gray")
pic.photo = img
pic.place(x=180, y=10)

# labels and entries to register

name_lbl = Label(window, fg="white", bg="gray", text="NAME: ")
name_lbl.place(x=190, y=172)

surname_lbl = Label(window, fg="white", bg="gray", text="SURNAME: ")
surname_lbl.place(x=190, y=222)

id_lbl = Label(window, fg="white", bg="gray", text="ID NUMBER: ")
id_lbl.place(x=190, y=272)

number_lbl = Label(window, fg="white", bg="gray", text="CONTACT: ")
number_lbl.place(x=190, y=322)

kin_lbl = Label(window, fg="white", bg="gray", text="NEXT OF KIN: ")
kin_lbl.place(x=190, y=372)

number2_lbl = Label(window, fg="white", bg="gray", text="CONTACT: ")
number2_lbl.place(x=190, y=422)


name_ent = Entry(window, fg="green", width=23)
name_ent.place(x=320, y=170)

surname_ent = Entry(window, fg="green", width=23)
surname_ent.place(x=320, y=220)

id_ent = Entry(window, fg="green", width=23)
id_ent.place(x=320, y=270)

number_ent = Entry(window, fg="green", width=23)
number_ent.place(x=320, y=320)

kin_ent = Entry(window, fg="green", width=23)
kin_ent.place(x=320, y=370)

number2_ent = Entry(window, fg="green", width=23)
number2_ent.place(x=320, y=420)

register_btn = Button(window, text="REGISTER", relief="raised", borderwidth=4, bg="white", width=10, height=1,)
register_btn.place(x=285, y=475)













window.mainloop()
