CREATE DATABASE IF NOT EXISTS tarea;
USE tarea;

CREATE TABLE IF NOT EXISTS alumnos(
    id_alumno INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    contrasena VARCHAR(100)
);

INSERT INTO alumnos (nombre, contrasena) VALUES('cako','123');
