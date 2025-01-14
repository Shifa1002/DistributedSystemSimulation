import sqlite3
import threading
import re
def create_tables():
    # Create Users Table
    with sqlite3.connect('databases/users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
    # Create Products Table
    with sqlite3.connect('databases/products.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)
    # Create Orders Table
    with sqlite3.connect('databases/orders.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Orders (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL
            )
        """)
    print("Tables created successfully.")
def validate_email(email):
    return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', email))

def validate_price(price):
    return price > 0

def validate_quantity(quantity):
    return quantity >= 0

def insert_users():
    users = [
        (1, "Alice", "alice@example.com"),
        (2, "Bob", "bob@example.com"),
        (3, "Charlie", "charlie@example.com"),
        (4, "David", "david@example.com"),
        (5, "Eve", "eve@example.com"),
        (6, "Frank", "frank@example.com"),
        (7, "Grace", "grace@example.com"),
        (8, "Alice", "alice@example.com"),
        (9, "Henry", "henry@example.com"),
        (10, "Jane", "jane@example.com")
    ]
    with sqlite3.connect('databases/users.db') as conn:
        cursor = conn.cursor()
        for user in users:
            if validate_email(user[2]):
                cursor.execute("INSERT INTO Users (id, name, email) VALUES (?, ?, ?)", user)
                print(f"Inserted User: {user}")
            else:
                print(f"Invalid email for user: {user}")
def insert_products():
    products = [
        (1, "Laptop", 1000.00),
        (2, "Smartphone", 700.00),
        (3, "Headphones", 150.00),
        (4, "Monitor", 300.00),
        (5, "Keyboard", 50.00),
        (6, "Mouse", 30.00),
        (7, "Laptop", 1000.00),
        (8, "Smartwatch", 250.00),
        (9, "Gaming Chair", 500.00),
        (10, "Earbuds", -50.00)
    ]
    with sqlite3.connect('databases/products.db') as conn:
        cursor = conn.cursor()
        for product in products:
            if validate_price(product[2]):
                cursor.execute("INSERT INTO Products (id, name, price) VALUES (?, ?, ?)", product)
                print(f"Inserted Product: {product}")
            else:
                print(f"Invalid price for product: {product}")
def insert_orders():
    orders = [
        (1, 1, 1, 2),
        (2, 2, 2, 1),
        (3, 3, 3, 5),
        (4, 4, 4, 1),
        (5, 5, 5, 3),
        (6, 6, 6, 4),
        (7, 7, 7, 2),
        (8, 8, 8, 0),
        (9, 9, 1, -1),
        (10, 10, 11, 2)
    ]
    with sqlite3.connect('databases/orders.db') as conn:
        cursor = conn.cursor()
        for order in orders:
            if validate_quantity(order[3]):
                cursor.execute("INSERT INTO Orders (id, user_id, product_id, quantity) VALUES (?, ?, ?, ?)", order)
                print(f"Inserted Order: {order}")
            else:
                print(f"Invalid quantity for order: {order}")
import threading

def main():
    create_tables()
    threads = [
        threading.Thread(target=insert_users),
        threading.Thread(target=insert_products),
        threading.Thread(target=insert_orders),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("All data insertion tasks are complete.")

if __name__ == "__main__":
    main()

def verify_data():
    print("\n--- Verifying Users Table ---")
    with sqlite3.connect('databases/users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users;")
        for row in cursor.fetchall():
            print(row)

    print("\n--- Verifying Products Table ---")
    with sqlite3.connect('databases/products.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products;")
        for row in cursor.fetchall():
            print(row)

    print("\n--- Verifying Orders Table ---")
    with sqlite3.connect('databases/orders.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Orders;")
        for row in cursor.fetchall():
            print(row)

if __name__ == "__main__":
    main()
    verify_data()




