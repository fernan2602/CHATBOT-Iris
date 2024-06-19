use TChatBot
go 
INSERT INTO TPersona (dni, nombre, apellido, correoElectronico, nroCelular,docente) 
VALUES 
('23983332','HUGO','ESPETIA HUAMANGA','23983332@CONTINENTAL.EDU.PE','999999999','si');

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


