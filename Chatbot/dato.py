import pyodbc

class BuscarDato():
    
    # Esta función define la búsqueda de un solo dato en nuestra Base de datos
    def execute_query(self, conexion, query):
        try:
            cursor = conexion.cursor()
            cursor.execute(query)
            row = cursor.fetchone()  # Obtener solo una fila
            cursor.close()
            
            if row:
                dato = row[0]  # Obtener el primer valor de la fila
                print(dato)
                return dato
            else:
                return None  # No se encontraron resultados
            
        except pyodbc.Error as e:
            print(f"Error al ejecutar la consulta: {str(e)}")
            return None