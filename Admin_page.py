# Demi-Leigh Jefferies Class 1
# Designing a program that allows users to login online
import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

# Creating the window

window = Tk()
window.title("ADMINISTRATOR")
window.geometry("700x600")
window.config(bg="gray")
window.resizable(0, 0)
window.wm_iconify()

# Adding an image on top
img = PhotoImage(file="Hnet.com-image.png")
pic = Label(window, image=img, height=110, bg="gray")
pic.photo = img
pic.place(x=180, y=10)

# Linking Python and SQL
mydb = mysql.connector.connect(user="lifechoices",
                               password="@Lifechoices1234", host="127.0.0.1", database="LifeChoicesOnline",
                               auth_plugin="mysql_native_password")
mycursor = mydb.cursor()


# Functionality for buttons
# Takes you to the window to add someone to register
def addpage():
    window.destroy()
    import adding


# Deletes an entry
def delete():
    window.iconify
    import delete


# Closes window
def exit():
    msg = messagebox.showinfo("NOTE", "You Will Now Return To The Main Screen")
    if msg == "ok":
        window.destroy()
        import Login


# Displays Register Table
def display_window():
    import database


# Checks how many people have signed in
def in_count():
    mycursor.execute("SELECT COUNT(Sign_In) FROM Login")
    for i in mycursor:
        in_lbl.config(text=i)


# Checks how many have signed out
def out_count():
    mycursor.execute("SELECT COUNT(Sign_Out) FROM Login")
    for i in mycursor:
        out_lbl.config(text=i)


# Clears the Sign In/Out count
def clear():
    in_lbl.config(text="")
    out_lbl.config(text="")


# Creating buttons so that admin can interact with database
add_btn = Button(window, text="ADD", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=addpage)
add_btn.place(x=100, y=150)

dlt_btn = Button(window, text="DELETE", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=delete)
dlt_btn.place(x=500, y=150)

display_btn = Button(window, text="DISPLAY", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=display_window)
display_btn.place(x=100, y=250)

exit_btn = Button(window, text="EXIT", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=exit)
exit_btn.place(x=500, y=250)

signIn_btn = Button(window, text="SIGNED IN", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=in_count)
signIn_btn.place(x=100, y=350)

signOut_btn = Button(window, text="SIGNED OUT", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=out_count)
signOut_btn.place(x=500, y=350)

in_lbl = tk.Label(window, bg="gray")
in_lbl.place(x=150, y=400)

out_lbl = tk.Label(window, bg="gray")
out_lbl.place(x=500, y=400)

clear_btn = Button(window, text="CLEAR", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=clear)
clear_btn.place(x=300, y=500)

window.mainloop()
