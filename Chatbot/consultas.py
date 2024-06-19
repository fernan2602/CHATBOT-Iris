
import pyodbc
from dato import BuscarDato
from connexion import Search

class Consultas():
    #Consultas a la base de datos
    #Select:
    def search_by_all(self,columna,tabla):
        db = Search()
        print(tabla+columna)
        conexion = db.connect()
        query = f'SELECT {tabla} from {columna}'
        Bd = BuscarDato()
        dato=Bd.execute_query(conexion,query)

        db.disconnect()
        
        print(dato)
        return dato
    


