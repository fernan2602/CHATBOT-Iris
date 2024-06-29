USE master
go 
-- Comando condicional para la base de datos

IF	DB_ID ('TChatBot') IS NOT NULL
DROP DATABASE TChatBot
GO
-- Crear la base de datos
CREATE DATABASE TChatBot;
GO

-- Usar la base de datos
USE TChatBot;
GO
-- Condicionales para las tablas 
if OBJECT_ID('TPersona') is not null
drop table TPersona
go

if OBJECT_ID('TAsignatura') is not null
drop table TAsignatura
go

if OBJECT_ID('THorario') is not null
drop table THorario
go


-- Crear la tabla Persona
CREATE TABLE TPersona (
    dni VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    correoElectronico VARCHAR(100),
    nroCelular VARCHAR(15),
<<<<<<< HEAD
    docente varchar(2),
    nota int 
=======
    docente varchar(2)
>>>>>>> 6a832e0b0b908f1eff423a4cb9d8ef209f6d3675
);
GO

-- Crear la tabla Asignatura
CREATE TABLE TAsignatura (
    NRC INT PRIMARY KEY,
    NombreAsignatura VARCHAR(100),
    DniProfesor varCHAR(20),
    FOREIGN KEY (DniProfesor) REFERENCES TPersona(dni)
);
GO

CREATE TABLE THorario (
    NRC INT,
    dia VARCHAR(15),
    hora varchar(100),
	Aula varchar(20),
	FOREIGN KEY (NRC) REFERENCES TAsignatura(NRC)
);

