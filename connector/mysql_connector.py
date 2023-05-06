import mysql.connector
from architecture.singleton import Singleton


class DBConnection(metaclass=Singleton):
    def __init__(self):
        # establish connection
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin",
            database="urlshortner",
        )
        # create a cursor object
        mycursor = mydb.cursor()
        # execute a query
        mycursor.execute("show databases;")
        # fetch results
        result = mycursor.fetchall()
        # print results
        for row in result:
            print(row)
