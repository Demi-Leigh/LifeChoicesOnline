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


def delete():
    dlt = "INSERT INTO Register(Name, Surname, Password, ID_Number, Contact_Number, NextOf_Kin, Kin_Number) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = ()
    mycursor.execute(dlt, values)
    mydb.commit()
    msg = messagebox.showinfo("NOTE", "User Deleted")


def back():
    window.destroy()
    import Admin_page
