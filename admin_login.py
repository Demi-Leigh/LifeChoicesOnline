# Demi-Leigh Jefferies Class 1
# Designing a program that allows users to login online
import mysql.connector
from tkinter import *
from tkinter import messagebox

# Creating the window

window = Tk()
window.title("ADMIN")
window.geometry("700x400")
window.config(bg="gray")
window.resizable(0, 0)


# Function for user to submit and log in as admin
def confirm():  # function to make sure correct details are entered
    if name_ent.get() == "lifechoices" and passw_ent.get() == "lifechoices1234":
        window.destroy()
        import Admin_page
    else:  # if incorrect name or password entered will tell user details are incorrect
        messagebox.showerror("ERROR", "Incorrect details entered")


# Adding an image on top
img = PhotoImage(file="Hnet.com-image.png")
pic = Label(window, image=img, height=110, bg="gray")
pic.photo = img
pic.place(x=180, y=10)

name_lbl = Label(window, fg="white", bg="gray", text="NAME: ")
name_lbl.place(x=180, y=170)

passw_lbl = Label(window, fg="white", bg="gray", text="PASSWORD: ")
passw_lbl.place(x=180, y=230)

name_ent = Entry(window, fg="green", width=25)
name_ent.place(x=290, y=170)

passw_ent = Entry(window, fg="green", width=25)
passw_ent.place(x=290, y=230)

confirm_btn = Button(window, text="CONFIRM", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=confirm)
confirm_btn.place(x=305, y=320)

window.mainloop()
