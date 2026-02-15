from Application.Database_Connection import get_connection
from Application.Products_dao import *

conn = get_connection()

products_dao(conn)

ch = input("Want to insert an item (y /n): ")
if(ch == 'y' or ch =='Y'):
    name = input("Product name: ")
    uom_id = int(input("uom_id: "))
    price = float(input("price/unit: "))

    insert_products(conn, name, uom_id, price)

ch = input("Want to delete an item (y /n): ")
if(ch == 'y' or ch =='Y'):
    id = input("Product id: ")

    delete_products(conn, id)

conn.close()
