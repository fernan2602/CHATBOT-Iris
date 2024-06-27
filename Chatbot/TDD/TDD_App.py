import unittest
from app import app, query_db

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_insertar_alumno(self):
        with app.test_request_context('/insertar', method='POST', data={
            'accion': 'Insertar',
            'nombre': 'Juan',
            'apellido': 'Pérez',
            'telefono': '123456789',
            'correo': 'juan@example.com',
            'dni': '12345678A',
            'nota': '15'
        }):
            rv = self.app.post('/insertar')
            self.assertIn(b'Juan', rv.data)
            self.assertIn(b'Pérez', rv.data)
            self.assertIn(b'12345678A', rv.data)
            # Añadir más assertions según sea necesario

    def test_eliminar_alumno(self):
        # Primero insertamos un alumno de prueba para eliminarlo luego
        query_insert = 'INSERT INTO TPersona (dni, nombre, apellido, correoElectronico, nroCelular, docente, nota) VALUES (?, ?, ?, ?, ?, ?, ?)'
        params_insert = ('12345678B', 'María', 'López', 'maria@example.com', '987654321', 'no', 12)
        query_db(query_insert, params_insert)

        with app.test_request_context('/insertar', method='POST', data={
            'accion': 'Eliminar',
            'dni': '12345678B'
        }):
            rv = self.app.post('/insertar')
            self.assertNotIn(b'María', rv.data)
            self.assertNotIn(b'López', rv.data)
            self.assertNotIn(b'12345678B', rv.data)
            # Añadir más assertions según sea necesario

    def test_actualizar_alumno(self):
        # Primero insertamos un alumno de prueba para actualizarlo luego
        query_insert = 'INSERT INTO TPersona (dni, nombre, apellido, correoElectronico, nroCelular, docente, nota) VALUES (?, ?, ?, ?, ?, ?, ?)'
        params_insert = ('12345678C', 'Carlos', 'Gómez', 'carlos@example.com', '654321987', 'no', 14)
        query_db(query_insert, params_insert)

        with app.test_request_context('/insertar', method='POST', data={
            'accion': 'Actualizar',
            'nombre': 'Carlos',
            'apellido': 'Martínez',
            'telefono': '654321987',
            'correo': 'carlos@example.com',
            'dni': '12345678C',
            'nota': '16'
        }):
            rv = self.app.post('/insertar')
            self.assertNotIn(b'Gómez', rv.data)
            self.assertIn(b'Martínez', rv.data)
            self.assertIn(b'16', rv.data)
            # Añadir más assertions según sea necesario

    def test_consultar_profesores(self):
        rv = self.app.get('/Profesor.html')
        self.assertEqual(rv.status_code, 200)
        # Añadir assertions para verificar que los profesores se están consultando correctamente

if __name__ == '__main__':
    unittest.main()