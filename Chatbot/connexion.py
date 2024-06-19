import pyodbc

class Search():
    def __init__(self):
        self.server = 'VICTORFERNANDO'
        self.database = 'TChatBot'
        
      #Apertura de conexion   
    def connect(self):
        try:
            conn_str = f'DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database}'
            self.conn = pyodbc.connect(conn_str)
            print("conexion exitosa")
            return self.conn
        except pyodbc.Error as e:
            print(f"Error al conectar a la base de datos: {str(e)}")

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("Conexión cerrada.")

    





    #Insert
    #Update
    #Delete

