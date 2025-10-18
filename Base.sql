-- Crear base de datos si no existe
CREATE DATABASE IF NOT EXISTS proyecto_crud;

USE proyecto_crud;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Tabla de productos
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2)
);

-- Insertamos un usuario de prueba
INSERT INTO users (username, password) VALUES ('admin', '1234');

-- Insertamos productos de prueba (opcional)
INSERT INTO products (name, description, price) VALUES
('Producto A','Descripción A',10.50),
('Producto B','Descripción B',20.75);

