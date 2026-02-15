def products_dao(connection):
    cursor = connection.cursor()

    query = """SELECT p.product_id, p.name, p.price_per_unit, u.uom_name
            FROM products AS p
            JOIN uom AS u ON p.uom_id = u.uom_id
            ORDER BY p.product_id ASC""" 
    cursor.execute(query)

    for product_id, name, price_per_unit, uom_name in cursor :
        print("ID: ",product_id, "| Name:",
              name, "| Price: ", 
              price_per_unit, uom_name)

    cursor.close()

def insert_products(connection, name, uom_id, price):
    cursor = connection.cursor();

    query = """INSERT INTO products(name, uom_id, price_per_unit)
               VALUES(%s, %s, %s)"""
    data = ( name, uom_id, price)
    cursor.execute(query, data);
    connection.commit()
    
    cursor.close()
    print("Item Inserted Successfully☑️")

def delete_products(connection,id):
    cursor = connection.cursor();

    query = """DELETE FROM products WHERE product_id = %s"""
    data = (id,)
    cursor.execute(query, data);
    connection.commit()
    
    cursor.close()
    print("Item Deleted Successfully☑️")