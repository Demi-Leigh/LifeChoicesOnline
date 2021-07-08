# Demi-Leigh Jefferies Class 1
# Designing a program that allows users to login online
import mysql.connector
from tkinter import *
import datetime

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

now = datetime.datetime.utcnow()


# Functions for the login page
mydb = mysql.connector.connect(user="lifechoices",
                               password="@Lifechoices1234", host="127.0.0.1", database="LifeChoicesOnline",
                               auth_plugin="mysql_native_password")
mycursor = mydb.cursor()


# Function to allow user to log in
def login():
    from datetime import datetime

    time = datetime.now()
    time = str(time)
    sql = "INSERT INTO Login (Name,Password,Sign_In, user_id)VALUES (%s, %s, %s, %s)"
    val = (name_ent.get(), password_ent.get(), time, 8)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


# Function to allow user to register
def register():
    window.destroy()
    import Register

# Function to sign out page
def sign_out():
    window.destroy()
    import Sign_out


# function to allow admin to log in
def admin_login():
    window.destroy()
    import admin_login


# Adding labels and entries for main screen to enter details
name_lbl = Label(window, fg="white", bg="gray", text="NAME: ")
name_lbl.place(x=240, y=170)

password_lbl = Label(window, fg="white", bg="gray", text="PASSWORD: ")
password_lbl.place(x=240, y=230)

name_ent = Entry(window, fg="green", width=25)
name_ent.place(x=380, y=170)

password_ent = Entry(window, fg="green", width=25)
password_ent.place(x=380, y=230)

# Adding Login, Register and Admin buttons

signIn_btn = Button(window, text="SIGN IN", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=login)
signIn_btn.place(x=70, y=330)

signOut_btn = Button(window, text="SIGN OUT", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=sign_out)
signOut_btn.place(x=250, y=330)

register_btn = Button(window, text="REGISTER", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=register)
register_btn.place(x=430, y=330)

admin_btn = Button(window, text="ADMIN", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=admin_login)
admin_btn.place(x=610, y=330)


window.mainloop()

