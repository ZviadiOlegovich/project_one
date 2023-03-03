import mysql.connector

# file = open("dbConfig.txt", encoding= "utf-8")
# t1 = file.readlines()


# db = mysql.connector.connect(t1)

# Настройки подключения к базе данных
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ford2008",
    database="todo",
    port="33306"
)
