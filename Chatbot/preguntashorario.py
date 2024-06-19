#Importar libreria de comparacion 
import difflib
from consultas import Consultas

class PreguntasHorario: 
        def __init__(self):
                
            self.base_conocimiento = {
        "dia":["dia", "fecha"],
        "hora":["hora","tiempo"],
        "Aula":[ "clase", "aula","salon"],
        "NRC":["nrc"]
        }

        def buscar_pregunta_similar(self,tabla,pregunta_completa):
            mejor_coincidencia = None
            mejor_similitud = 0.0
        #Como tenemos la consulta en oracion divida en una array con n palabras 
        #Verificaremos las similitudes con glsario de respuestas
        #Creacion de un bucle que recorre todas las preguntas y respuestas predeterminadas
            for pregunta_usuario in pregunta_completa:
            #Entra al bucle palabra por palabra
               for respuesta, preguntas in self.base_conocimiento.items():

                # Compara la pregunta usuario utilizando la palabra preguntas 
                    for pregunta in preguntas:
                    #Utilizando un comando de la librerio difflib comparamos pregunta[n] con la pregunta_usuario
                        similitud = difflib.SequenceMatcher(None, pregunta_usuario, pregunta).ratio()
                        #Evaluamos la similitud
                        if similitud > mejor_similitud:
                            mejor_similitud = similitud
                            mejor_coincidencia = respuesta
            
        #Ponemos un minimo del 80% para comprobar similitud
            if mejor_coincidencia and mejor_similitud >= 0.8: 
                # Realizar la consulta con los atributos heredados
                cPersona = Consultas()
                print(mejor_coincidencia)
                dato = cPersona.search_by_all(tabla,mejor_coincidencia)
                print(dato)
                return  dato
              
                
    