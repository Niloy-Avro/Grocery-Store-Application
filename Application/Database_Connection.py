import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        user="root",
        password="niloy",
        host="127.0.0.1",
        database="GroceryStore"
    )

    return connection