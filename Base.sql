CREATE DATABASE proyecto_crud;

USE proyecto_crud;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2)
);

-- Insertamos un usuario de prueba
INSERT INTO users (username, password) VALUES ('admin', '1234');
