import mysql.connector

lepDB = mysql.connector.connect(
    host="localhost",
    user="kyouma",
    password="root",
    port="3306",
)

def createDB():
    lepCursor = lepDB.cursor()
    lepCursor.execute("CREATE DATABASE lepDatabase")
    lepCursor.close()
