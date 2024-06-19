# Conciderare similitud con la palabra clave para optimizar las respuestas del chat
# Esta libreria compara las preguntas en un indice calculado cual es la más cercana para dar una solucion
import difflib

#Importaremos  la clase de herencia PreguntaPersona
from preguntaspersona import PreguntasPersona
from preguntashorario import PreguntasHorario
from preguntasasignatura import PreguntasAsignatura

# Ejemplo de preguntas y respuestas
class Preguntas: 
     
    def __init__(self):
        self.base_conocimiento = {
        "Hola soy tu asistente personal":["hola", "hello", "q hay"],
        "TPersona":["profesor", "maestro","docente"],
        "TAsignatura":[ "curso", "asignatura","materia"],
        "THorario":["hora","dia","lugar"]
        }
        
        

    def buscar_pregunta_similar(self,pregunta_completa):
        
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
            #Crear bucle de coincidencias para buscar la respuesta exacta 
            #Comando if para el TPersona
            if mejor_coincidencia == "TPersona":
                #Nombrar PreguntasPersona
                Consulta = PreguntasPersona()
                print(mejor_coincidencia)
                Respuesta = Consulta.buscar_pregunta_similar(mejor_coincidencia,pregunta_completa)
                print(Respuesta)
                return  Respuesta
            if mejor_coincidencia == "TAsignatura":
                #Nombrar PreguntasPersona
                Consulta = PreguntasAsignatura()
                print(mejor_coincidencia)
                Respuesta = Consulta.buscar_pregunta_similar(mejor_coincidencia,pregunta_completa)
                print(Respuesta)
                return  Respuesta
            if mejor_coincidencia == "THorario":
                #Nombrar PreguntasPersona
                Consulta = PreguntasHorario()
                print(mejor_coincidencia)
                Respuesta = Consulta.buscar_pregunta_similar(mejor_coincidencia,pregunta_completa)
                print(Respuesta)
                return  Respuesta
            else:
                return mejor_coincidencia
               
        
            
       



