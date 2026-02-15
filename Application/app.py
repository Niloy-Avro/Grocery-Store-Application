from flask import Flask, render_template, request, redirect, session
from Database_Connection import get_connection
from Products_dao import *

app = Flask(__name__)

"""Home Page"""

@app.route("/")
def home() :
    return render_template("index.html")



"""ADMIN Page operations"""

@app.route("/admin")
def admin() : 
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT p.product_id, p.name, p.price_per_unit, u.uom_name
        FROM products AS p
        JOIN uom AS u ON p.uom_id = u.uom_id
        ORDER BY p.product_id ASC
    """

    cursor.execute(query)
    products = cursor.fetchall()

    #Creating UOM name dropdown List
    query1 = """
        SELECT uom_id, uom_name FROM uom
    """

    cursor.execute(query1)
    uoms = cursor.fetchall()

    conn.close()

    return render_template (
        "admin.html", 
        products = products,
        uoms = uoms
    )


@app.route("/add", methods=["POST"])
def add_product() : 
    name = request.form["name"]
    uom_name = request.form["uom_name"]
    price = request.form["price"]

    conn = get_connection()
    insert_products(conn, name, uom_name, price)
    conn.close()

    return redirect("/admin")


@app.route("/delete/<id>")
def delete_product(id) : 
    conn = get_connection()
    delete_products(conn, id)
    conn.close()

    return redirect("/admin")


@app.route("/reset")
def reset_database():

    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE products")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

    conn.commit()
    conn.close()

    return redirect("/admin")


"""CUSTOMER page operations"""

@app.route("/customer")
def customer_page():
    conn = get_connection();
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT p.product_id, p.name, p.price_per_unit, u.uom_name
        FROM products AS p
        JOIN uom AS u ON u.uom_id = p.uom_id
    """

    cursor.execute(query)
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("customer.html", products=products)


"""Cart Scetion"""

@app.route("/cart")
def cart():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT p.name, c.quant, u.uom_name,
               (c.quant * p.price_per_unit) AS total_price
        FROM cart c
        JOIN products p ON p.product_id = c.product_id
        JOIN uom u ON u.uom_id = p.uom_id
    """

    cursor.execute(query)
    cart_items = cursor.fetchall()

    grand_total = sum(item["total_price"] for item in cart_items)

    conn.close()

    return render_template(
        "cart.html",
        cart_items=cart_items,
        grand_total=grand_total
    )

@app.route("/addCart/<int:product_id>")
def addCart(product_id):

    conn = get_connection()
    cursor = conn.cursor()

    # Check if already exists
    cursor.execute(
        "SELECT quant FROM cart WHERE product_id = %s",
        (product_id,)
    )

    result = cursor.fetchone()

    if result:
        cursor.execute(
            "UPDATE cart SET quant = quant + 1 WHERE product_id = %s",
            (product_id,)
        )
    else:
        cursor.execute(
            "INSERT INTO cart (product_id, quant) VALUES (%s, 1)",
            (product_id,)
        )

    conn.commit()
    conn.close()

    return redirect("/customer")

@app.route('/checkout')
def checkout() :
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("TRUNCATE TABLE cart")

    conn.commit()
    conn.close()
    cursor.close()

    return redirect('/')

"""main"""

if __name__ == "__main__" :
    app.run(debug = True)