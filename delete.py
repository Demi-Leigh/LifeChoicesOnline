# Demi-Leigh Jefferies Class 1
# Designing a program that allows users to login online
import mysql.connector
from tkinter import *
from tkinter import messagebox

# Creating the window

window = Tk()
window.title("ADMINISTRATOR")
window.geometry("700x400")
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
    dlt = "DELETE FROM Login WHERE ID_Number=" + id_ent.get()
    mycursor.execute(dlt)
    mydb.commit()

    dlt = "DELETE FROM Register WHERE ID_Number=" + id_ent.get()
    mycursor.execute(dlt)
    mydb.commit()
    msg = messagebox.showinfo("NOTE", "User Deleted")
    if msg == "ok":
        id_ent.delete(0, END)


def back():
    window.destroy()
    import Admin_page


id_lbl = Label(window, fg="white", bg="gray", text="ID NUMBER: ")
id_lbl.place(x=190, y=172)

id_ent = Entry(window, fg="green", width=23)
id_ent.place(x=360, y=170)

# surname_lbl = Label(window, fg="white", bg="gray", text="SURNAME: ")
# surname_lbl.place(x=190, y=200)
#
# surname_ent = Entry(window, fg="green", width=23)
# surname_ent.place(x=360, y=200)


dlt_btn = Button(window, text="DELETE", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=delete)
dlt_btn.place(x=190, y=300)

return_btn = Button(window, text="RETURN", relief="raised", borderwidth=4, bg="white", width=10, height=1, command=back)
return_btn.place(x=400, y=300)

window.mainloop()
