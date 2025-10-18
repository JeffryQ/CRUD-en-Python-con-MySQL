import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='proyecto_crud',
            user='TU USUARIO',        # Cambia si tu usuario es otro
            password='TU CONTRASEÑA'   # Cambia tu contraseña
        )
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
