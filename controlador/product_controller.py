from modelos.db import get_connection

class ProductController:
    @staticmethod
    def get_products():
        conn = get_connection()
        products = []
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            cursor.close()
            conn.close()
        return products

    @staticmethod
    def get_product(product_id):
        conn = get_connection()
        product = None
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE id=%s", (product_id,))
            product = cursor.fetchone()
            cursor.close()
            conn.close()
        return product

    @staticmethod
    def create_product(name, description, price):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (name, description, price) VALUES (%s, %s, %s)", (name, description, price))
            conn.commit()
            cursor.close()
            conn.close()

    @staticmethod
    def update_product(product_id, name, description, price):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET name=%s, description=%s, price=%s WHERE id=%s", (name, description, price, product_id))
            conn.commit()
            cursor.close()
            conn.close()

    @staticmethod
    def delete_product(product_id):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
            conn.commit()
            cursor.close()
            conn.close()
