use TChatBot
go 
INSERT INTO TPersona (dni, nombre, apellido, correoElectronico, nroCelular,docente) 
VALUES 
('23983332','HUGO','ESPETIA HUAMANGA','23983332@CONTINENTAL.EDU.PE','999999999','si');
('11111111', 'Juan', 'Gómez', 'juan@gmail.com', '987654321', 'no', 15),
('22222222', 'María', 'López', 'maria@gmail.com', '654321987', 'no', 12),
('33333333', 'Carlos', 'Martínez', 'carlos@gmail.com', '789456123', 'no', 18),
('44444444', 'Ana', 'Rodríguez', 'ana@gmail.com', '321654987', 'no', 14),
('55555555', 'Pedro', 'Sánchez', 'pedro@gmail.com', '963258741', 'no', 16),
('66666666', 'Laura', 'García', 'laura@gmail.com', '147258369', 'no', 19),
('77777777', 'Pablo', 'Fernández', 'pablo@gmail.com', '852963147', 'no', 17),
('88888888', 'Sara', 'Díaz', 'sara@gmail.com', '369852147', 'no', 13),
('10101010', 'Elena', 'Hernández', 'elena@gmail.com', '258741369', 'no', 15);

INSERT INTO TAsignatura (NRC, NombreAsignatura, DniProfesor) 
VALUES 
(12860,'CONSTRUCCION DE SOFTWARE','23983332')


INSERT INTO THorario (NRC, dia,hora,aula)
VALUES
(12860,'MIERCOLES','14:00 pm - 15:30 pm','A306'),
(12860,'JUEVES','14:00 pm - 16:30 pm','A801');




select * from TPersona
select * from TAsignatura
SELECT * FROM THorario


