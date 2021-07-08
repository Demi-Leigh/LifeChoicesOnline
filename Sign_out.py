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
mydb = mysql.connector.connect(user="lifechoices",
                                   password="@Lifechoices1234", host="127.0.0.1", database="LifeChoicesOnline",
                                   auth_plugin="mysql_native_password")
mycursor = mydb.cursor()


# Functions for the login page
def sign_out():
    from datetime import datetime

    time = datetime.now()
    time = str(time)
    sql = "UPDATE Login SET Sign_Out=" + time + " WHERE Password=" + password_ent.get() + ""
    mycursor.execute(sql)
    mydb.commit()


message = Label(window, text="CURRENTLY SIGNED IN", bg="gray")
message.place(x=325, y=150)

password_lbl = Label(window, text="Enter Password please: ", bg="gray")
password_lbl.place(x=325, y=200)

password_ent = Entry(window)
password_ent.place(x=325, y=250)

sign_out_btn = Button(window, text="Sign Out", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=sign_out)
sign_out_btn.place(x=350, y=330)

window.mainloop()
