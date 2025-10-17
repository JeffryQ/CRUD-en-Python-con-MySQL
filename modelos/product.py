from modelos.db import get_connection

class Product:
    @staticmethod
    def create(name, description, price):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (name, description, price) VALUES (%s, %s, %s)",
                           (name, description, price))
            conn.commit()
            conn.close()

    @staticmethod
    def read_all():
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            results = cursor.fetchall()
            conn.close()
            return results

    @staticmethod
    def read_one(product_id):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE id=%s", (product_id,))
            result = cursor.fetchone()
            conn.close()
            return result

    @staticmethod
    def update(product_id, name, description, price):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET name=%s, description=%s, price=%s WHERE id=%s",
                           (name, description, price, product_id))
            conn.commit()
            conn.close()

    @staticmethod
    def delete(product_id):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
            conn.commit()
            conn.close()
