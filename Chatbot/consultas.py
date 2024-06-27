
import pyodbc
from dato import BuscarDato
from connexion import Search

class Consultas():
    #Consultas a la base de datos
    #Consulta busqueda en tablas
    def search_by_all(self,columna,tabla,params =None):
        db = Search()
        Bd = BuscarDato()

        conexion = db.connect()
        query = f'SELECT {columna} from {tabla}'

        if params :
            query +=f' WHERE docente =  ?'
            dato=  Bd.execute_query(conexion, query, params)
            print(dato)
            db.disconnect()
        else :
            dato = Bd.execute_query(conexion, query)
            db.disconnect()

        return dato
    
        
    


