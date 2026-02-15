def products_dao(connection):
    cursor = connection.cursor()

    query = """SELECT p.product_id, p.name, p.price_per_unit, u.uom_name
            FROM products AS p
            JOIN uom AS u ON p.uom_id = u.uom_id
            ORDER BY p.product_id ASC""" 
    cursor.execute(query)

    for product_id, name, price_per_unit, uom_name in cursor :
        print("ID: ",product_id, "| Name:",name, "| Price: ", price_per_unit, uom_name)
