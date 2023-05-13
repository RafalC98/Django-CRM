import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456'
    )

#prepare a cursos object

cursorObject = dataBase.cursor()

#create a database

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")