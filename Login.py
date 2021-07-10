# Demi-Leigh Jefferies Class 1
# Designing a program that allows users to login online
import mysql.connector
from tkinter import *
import datetime
from tkinter import messagebox

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


# Linking Python and SQL
mydb = mysql.connector.connect(user="lifechoices",
                               password="@Lifechoices1234", host="127.0.0.1", database="LifeChoicesOnline",
                               auth_plugin="mysql_native_password")
mycursor = mydb.cursor()


# Checks for the user in the login table and signs that specific user in
# Then imports the sign out window for user to sign out later
def sign_in():
    global mycursor
    mycursor.execute("SELECT * FROM Login WHERE Name='" + name_ent.get() + "' AND Password='" + password_ent.get() + "'")
    mycursor = mycursor.fetchall()

    for i in mycursor:
        if name_ent.get() in i and password_ent.get() in i:
            cursor = mydb.cursor()
            sql = "UPDATE Login SET Sign_In = curtime() WHERE Password='" + password_ent.get() + "'"
            cursor.execute(sql)
            print(cursor.rowcount, "time-recorded")
            mydb.commit()
            msg = messagebox.showinfo("NOTE", "Login Successful! Enjoy Your Day")
            if msg == "ok":
                window.destroy()
                import Sign_out


# Takes the user to the register window
def register():
    window.destroy()
    import Register


# Takes the user to the sign out page
def exit():
    msg = messagebox.showinfo("GOODBYE", "Goodbye Enjoy The Rest Of Your Day")
    if msg == "ok":
        window.destroy()


# function to allow admin to log in
def admin_login():
    window.destroy()
    import admin_login


# Adding labels and entries for main screen to enter details
name_lbl = Label(window, fg="white", bg="gray", text="NAME: ")
name_lbl.place(x=240, y=170)

password_lbl = Label(window, fg="white", bg="gray", text="PASSWORD: ")
password_lbl.place(x=240, y=210)

name_ent = Entry(window, fg="green", width=25)
name_ent.place(x=380, y=170)

password_ent = Entry(window, fg="green", width=25)
password_ent.place(x=380, y=210)

# Adding Login, Register and Admin buttons

signIn_btn = Button(window, text="SIGN IN", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=sign_in)
signIn_btn.place(x=70, y=330)

register_btn = Button(window, text="REGISTER", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=register)
register_btn.place(x=250, y=330)

admin_btn = Button(window, text="ADMIN", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=admin_login)
admin_btn.place(x=430, y=330)

exit_btn = Button(window, text="EXIT", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=exit)
exit_btn.place(x=610, y=330)


window.mainloop()

