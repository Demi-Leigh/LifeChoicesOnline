# Demi-Leigh Jefferies Class 1
# Designing a program that allows users to login online
import mysql.connector
from tkinter import *

# Creating the window

window = Tk()
window.title("ADMINISTRATOR")
window.geometry("700x440")
window.config(bg="gray")
window.resizable(0, 0)

# Creating main screen to either register or login
# Adding an image on top
img = PhotoImage(file="Hnet.com-image.png")
pic = Label(window, image=img, height=110, bg="gray")
pic.photo = img
pic.place(x=180, y=10)


# Functionality for buttons
def addpage():
    window.destroy()
    import adding


# Creating buttons so that admin can interact with database
add_btn = Button(window, text="ADD", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=addpage)
add_btn.place(x=50, y=150)

edit_btn = Button(window, text="EDIT", relief="raised", borderwidth=4, bg="white", width=10, height=1)
edit_btn.place(x=50, y=250)

dlt_btn = Button(window, text="DELETE", relief="raised", borderwidth=4, bg="white", width=10, height=1)
dlt_btn.place(x=50, y=350)

exit_btn = Button(window, text="EXIT", relief="raised", borderwidth=4, bg="white", width=10, height=1)
exit_btn.place(x=500, y=350)

window.mainloop()
