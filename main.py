# Demi-Leigh Jefferies Class 1
# Designing a program that allows users to login online
import mysql.connector
from tkinter import *



mydb = mysql.connector.connect(user="lifechoices",
                               password="@Lifechoices1234", host="127.0.0.1", database="LifeChoicesOnline",
                               auth_plugin="mysql_native_password")
mycursor = mydb.cursor()
sql = "INSERT INTO Register VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
val = ("GDP", "Godwin", "9501230185082", "0735887757", "gdsg", "0679715026", "14:22", "14:45")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, " record inserted.")
mycursor.execute("Select * from Register")
for i in mycursor:
    print(i)

