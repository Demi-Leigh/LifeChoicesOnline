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


# Functions for the login page
mydb = mysql.connector.connect(user="lifechoices",
                               password="@Lifechoices1234", host="127.0.0.1", database="LifeChoicesOnline",
                               auth_plugin="mysql_native_password")
mycursor = mydb.cursor()


def sign_in():
    global mycursor
    mycursor.execute("SELECT * FROM Login")
    mycursor = mycursor.fetchall()

    for i in mycursor:
        if name_ent.get() in i and password_ent.get() in i:
            window.destroy()
            cursor = mydb.cursor()
            sql = "UPDATE Login SET Sign_In = curtime();"
            cursor.execute(sql)
            print(cursor.rowcount, "time-recorded")
            mydb.commit()
            import Sign_out
            print(Sign_out)
        else:
            name_ent.delete(0, END)
            id_ent.delete(0, END)
            messagebox.showerror("Check Your Details", "Check Your Details" + "\n"
                                 + "Check With The Admin To See If You In The Database")


# Function to allow user to log in
def login():
    from datetime import datetime

    time = datetime.now()
    time = str(time)
    mycursor.execute("SELECT user_id FROM Register WHERE Name='" + name_ent.get() + "' AND ID_Number='" + id_ent.get() + "'")
    user_id = mycursor.fetchall()[0][0]
    print(user_id)
    sql = "INSERT INTO Login (Name, Password,user_id,Sign_In, ID_Number) VALUES (%s, %s, %s, %s, %s)"
    val = (name_ent.get(), password_ent.get(), user_id, time, id_ent.get())
    mycursor.execute(sql, val)
    mydb.commit()
    msg = messagebox.showinfo("NOTE", "Logged Successfully")
    if msg == "ok":
        import Sign_out


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
password_lbl.place(x=240, y=210)

id_lbl = Label(window, fg="white", bg="gray", text="ID NUMBER")
id_lbl.place(x=240, y=250)

name_ent = Entry(window, fg="green", width=25)
name_ent.place(x=380, y=170)

password_ent = Entry(window, fg="green", width=25)
password_ent.place(x=380, y=210)

id_ent = Entry(window, fg="green", width=25)
id_ent.place(x=380, y=250)


# Adding Login, Register and Admin buttons

signIn_btn = Button(window, text="SIGN IN", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=sign_in)
signIn_btn.place(x=70, y=330)

signOut_btn = Button(window, text="SIGN OUT", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=sign_out)
signOut_btn.place(x=250, y=330)

register_btn = Button(window, text="REGISTER", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=register)
register_btn.place(x=430, y=330)

admin_btn = Button(window, text="ADMIN", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=admin_login)
admin_btn.place(x=610, y=330)


window.mainloop()

