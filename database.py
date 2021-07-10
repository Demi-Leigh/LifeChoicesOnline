# Demi-Leigh Jefferies Class 1
# Designing a program that allows users to login online
import mysql.connector
import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title("ADMINISTRATOR")
window.geometry("690x500")
window.config(bg="gray")
window.resizable(0, 0)

mydb = mysql.connector.connect(user="lifechoices",
                               password="@Lifechoices1234", host="127.0.0.1", database="LifeChoicesOnline",
                               auth_plugin="mysql_native_password")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Register limit 0,10")
i = 0
for user in mycursor:
    for j in range(len(user)):
        e = Entry(window, width=10, fg='white', bg="gray")
        e.grid(row=i, column=j)
        e.insert(END, user[j])
    i = i+1

window.mainloop()
