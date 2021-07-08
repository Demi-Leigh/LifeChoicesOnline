# Demi-Leigh Jefferies Class 1
# Designing a program that allows users to login online
import mysql.connector
from tkinter import *
from tkinter import messagebox

# Creating the window

window = Tk()
window.title("ADMINISTRATOR")
window.geometry("700x600")
window.config(bg="gray")
window.resizable(0, 0)

# Adding an image on top
img = PhotoImage(file="Hnet.com-image.png")
pic = Label(window, image=img, height=110, bg="gray")
pic.photo = img
pic.place(x=180, y=10)


# linking mysql and python
mydb = mysql.connector.connect(user="lifechoices",
                               password="@Lifechoices1234", host="127.0.0.1", database="LifeChoicesOnline",
                               auth_plugin="mysql_native_password")
mycursor = mydb.cursor()


def adding():
    add = "INSERT INTO Register(Name, Surname, Password, ID_Number, Contact_Number, NextOf_Kin, Kin_Number) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (name_ent.get(), surname_ent.get(), password_ent.get(), id_number_ent.get(), contact_ent.get(), nextof_ent.get(), contact2_ent.get())
    mycursor.execute(add, values)
    mydb.commit()
    msg = messagebox.showinfo("NOTE", "Submission Added")
    if msg == "ok":
        name_ent.delete(0, END)
        surname_ent.delete(0, END)
        password_ent.delete(0, END)
        id_number_ent.delete(0, END)
        contact_ent.delete(0, END)
        nextof_ent.delete(0, END)
        contact2_ent.delete(0, END)


def back():
    window.destroy()
    import Admin_page


name_lbl = Label(window, fg="white", bg="gray", text="NAME: ")
name_lbl.place(x=190, y=172)

surname_lbl = Label(window, fg="white", bg="gray", text="SURNAME: ")
surname_lbl.place(x=190, y=222)

password_lbl = Label(window, fg="white", bg="gray", text="PASSWORD: ")
password_lbl.place(x=190, y=272)

id_number_lbl = Label(window, fg="white", bg="gray", text="ID NUMBER: ")
id_number_lbl.place(x=190, y=322)

contact_lbl = Label(window, fg="white", bg="gray", text="CONTACT NUMBER: ")
contact_lbl.place(x=190, y=372)

kin_lbl = Label(window, fg="white", bg="gray", text="NEXT OF KIN: ")
kin_lbl.place(x=190, y=422)

number_lbl = Label(window, fg="white", bg="gray", text="NEXT OF KIN CONTACT: ")
number_lbl.place(x=190, y= 470)


name_ent = Entry(window, fg="green", width=23)
name_ent.place(x=360, y=170)

surname_ent = Entry(window, fg="green", width=23)
surname_ent.place(x=360, y=220)

password_ent = Entry(window, fg="green", width=23)
password_ent.place(x=360, y=270)

id_number_ent = Entry(window, fg="green", width=23)
id_number_ent.place(x=360, y=320)

contact_ent = Entry(window, fg="green", width=23)
contact_ent.place(x=360, y=370)

nextof_ent = Entry(window, fg="green", width=23)
nextof_ent.place(x=360, y=420)

contact2_ent = Entry(window, fg="green", width=23)
contact2_ent.place(x=360, y=470)

add_btn = Button(window, text="ADD", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=adding)
add_btn.place(x=190, y=540)

return_btn = Button(window, text="RETURN", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=back)
return_btn.place(x=400, y=540)
window.mainloop()
