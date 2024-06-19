import pyodbc

class Database:
    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.conn = None
        self.connect()

    def connect(self):
        try:
            conn_str = f'DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database}'
            self.conn = pyodbc.connect(conn_str)
            
        except pyodbc.Error as e:
            print(f"Error al conectar a la base de datos: {str(e)}")

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("Conexión cerrada.")
    
    def execute_query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except pyodbc.Error as e:
            print(f"Error al ejecutar la consulta: {str(e)}")
            return None
# Ejemplo de uso
