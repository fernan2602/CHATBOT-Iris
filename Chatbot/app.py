from flask import Flask, request, render_template, jsonify
from preguntas import Preguntas
import pyodbc
#Instalar nueva libreria para poder usar las tablas de la base de datos
from connexion import Search
from ia import  IAConsultas


app = Flask(__name__)

# Función para ejecutar consultas SQL
def query_db(query, params = None , select=False):
    db = Search()
    conn = db.connect()
    cursor = conn.cursor()
    
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        if select:
            rows = cursor.fetchall()
            return rows
        else:
            conn.commit()
            return None
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()
    
    

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({"error": "Bad Request", "message": "No question provided"}), 400
    
    pregunta_usuario = data['question']

    pPractica = Preguntas()
    
    for clave  in pregunta_usuario.split():
        print (clave)
        if clave == "chat" and "ayudame" and "iris":
            dato_2 = ia(pregunta_usuario)
            return jsonify({"response":dato_2})
            
    dato = pPractica.buscar_pregunta_similar(pregunta_usuario.split())   
    return jsonify({"response":dato})  
    
    
    

    # Suponiendo que Preguntas() es una clase y buscar_pregunta_similar es un método de esa clase
    
def ia(pregunta_usuario):
    salida = 'True'
    while salida == 'True':
        pregunta = pregunta_usuario
        data = request.get_json()
        
        if pregunta == "adios"or "salir" or "exit":
            salida = 'False'

        IA = IAConsultas()
        dato = IA.obtener_respuesta(pregunta)


        return dato
    
    

    




@app.route('/Profesor.html', methods=['GET'])
def Profesor():
    try:
        # Consultar estudiantes desde SQL Server filtrando por docente no "si"
        query = 'SELECT dni, nombre, apellido, correoElectronico, nroCelular, nota FROM TPersona WHERE docente <> ?'
        params = ('si',)
        estudiantes = query_db(query, params=params, select=True)
        return render_template('Profesor.html', estudiantes=estudiantes, mensaje=None)
    except Exception as e:
        return f"Error al consultar la base de datos: {str(e)}", 500
    
@app.route('/insertar', methods=['POST'])   
def insertar():
    if request.method == 'POST':
        accion = request.form['accion']
        
        try:
            if accion == 'Insertar':
                # Obtener datos del formulario para la inserción
                nombre = request.form['nombre']
                apellido = request.form['apellido']
                telefono = request.form['telefono']
                correo = request.form['correo']
                dni = request.form['dni']
                nota = request.form['nota']
                docente = "no"

                # Validar que todos los campos requeridos estén llenos
                if not (nombre and apellido and telefono and correo and dni and nota):
                    raise ValueError('Todos los campos son requeridos para insertar.')

                # Preparar y ejecutar la consulta SQL de inserción
                query_insert = 'INSERT INTO TPersona (dni, nombre, apellido, correoElectronico, nroCelular, docente, nota) VALUES (?, ?, ?, ?, ?, ?, ?)'
                params_insert = (dni, nombre, apellido, correo, telefono, docente, nota)
                query_db(query_insert, params_insert)

            elif accion == 'Eliminar':
                # Obtener el DNI del formulario para eliminar el registro correspondiente
                dni_eliminar = request.form['dni']
                
                if not dni_eliminar:
                    raise ValueError('Debe proporcionar un DNI para eliminar.')

                # Preparar y ejecutar la consulta SQL de eliminación
                query_delete = 'DELETE FROM TPersona WHERE dni = ?'
                params_delete = (dni_eliminar,)
                query_db(query_delete, params_delete)

            elif accion == 'Actualizar':
                # Obtener datos del formulario para la actualización
                nombre = request.form['nombre']
                apellido = request.form['apellido']
                telefono = request.form['telefono']
                correo = request.form['correo']
                dni = request.form['dni']
                nota = request.form['nota']

                # Validar que todos los campos requeridos estén llenos para actualizar
                if not (nombre and apellido and telefono and correo and dni and nota):
                    raise ValueError('Todos los campos son requeridos para actualizar.')

                # Preparar y ejecutar la consulta SQL de actualización
                query_update = 'UPDATE TPersona SET nombre = ?, apellido = ?, correoElectronico = ?, nroCelular = ?, nota = ? WHERE dni = ?'
                params_update = (nombre, apellido, correo, telefono, nota, dni)
                query_db(query_update, params_update)

            # Consultar estudiantes después de cualquier operación CRUD para mostrar en la plantilla
            query_select = 'SELECT dni, nombre, apellido, correoElectronico, nroCelular, nota FROM TPersona WHERE docente <> ?'
            params_select = ('si',)
            estudiantes = query_db(query_select, params=params_select)

            return render_template('Profesor.html', estudiantes=estudiantes, mensaje=None)

        except ValueError as ve:
            # Captura específica para errores de campos vacíos
            mensaje = str(ve)
            return render_template('Profesor.html', estudiantes=None, mensaje=mensaje)

        except Exception as e:
            # Captura genérica para cualquier otra excepción no manejada
            mensaje = f'Error: {str(e)}'
            return render_template('Profesor.html', estudiantes=None, mensaje=mensaje)

    # Redirigir a Profesor.html en caso de cualquier error o situación no esperada
    return redirect(url_for('Profesor'))

if __name__ == '__main__':
    app.run(debug=True)










