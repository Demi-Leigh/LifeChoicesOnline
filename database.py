# Demi-Leigh Jefferies Class 1
# Designing a program that allows users to login online
import mysql.connector
import tkinter as tk
from tkinter import *


# Creating the window
window = tk.Tk()
window.title("ADMINISTRATOR")
window.geometry("1000x500")
window.config(bg="gray")
window.resizable(0, 0)

# Linking Python and SQL

mydb = mysql.connector.connect(user="lifechoices",
                               password="@Lifechoices1234", host="127.0.0.1", database="LifeChoicesOnline",
                               auth_plugin="mysql_native_password")
mycursor = mydb.cursor()

# Labels for headings of columns
name = Label(window, width=15, text='Name', borderwidth=2, relief='raised', anchor='w', bg='white')
name.grid(row=0, column=0)

surname = Label(window, width=15, text='Surname', borderwidth=2, relief='raised', anchor='w', bg='white')
surname.grid(row=0, column=1)

password = Label(window, width=15, text='Password', borderwidth=2, relief='raised', anchor='w', bg='white')
password.grid(row=0, column=2)

id = Label(window, width=15, text='ID_Number', borderwidth=2, relief='raised', anchor='w', bg='white')
id.grid(row=0, column=3)

contact = Label(window, width=15, text='Contact_Number', borderwidth=2, relief='raised', anchor='w', bg='white')
contact.grid(row=0, column=4)

nextof = Label(window, width=15, text='NextOf_Kin', borderwidth=2, relief='raised', anchor='w', bg='white')
nextof.grid(row=0, column=5)

kin_contact = Label(window, width=15, text='Kin_Number', borderwidth=2, relief='raised', anchor='w', bg='white')
kin_contact.grid(row=0, column=6)

user_id = Label(window, width=15, text='user_id', borderwidth=2, relief='raised', anchor='w', bg='white')
user_id.grid(row=0, column=7)

i = 1

# Looping through all entries in the Register table and displaying it
mycursor.execute("SELECT * FROM Register limit 0,50")
for user in mycursor:
    for j in range(len(user)):
        data = Entry(window, width=15, fg='white', bg="gray")
        data.grid(row=i, column=j)
        data.insert(END, user[j])
    i = i+1

window.mainloop()
