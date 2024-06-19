import difflib

class Respuesta: 
    def __init__(self):
        self.afirmaciones= {
            1:["si", "yes", "claro"],
            2:["jamas", "nunca", "no"],

        }
        #Creare las variables statics

        
 
    def Investigar(self,respuesta):
        if respuesta=="TPersona":
            #self.PreguntaTablaHorario()
                print("Hola consultor, ¿Es usted el docente?")
                respuesta = input("Responda si o no: ")              
                resultado = self.buscar_Respuesta(respuesta)
                return resultado
     
        else:
            if respuesta =="THorario":
                #self.PreguntaTablaHorario()
                print("Hola consultor, ¿Es usted el docente?")
                respuesta = input("Responda si o no: ")
                resultado= self.buscar_Respuesta(respuesta)
                return resultado
              
            else:
                if respuesta =="TAsignatura":
                   #self.PreguntaTablaAsignatura()
                   
                   return "falso"

    def buscar_Respuesta(self,pregunta_usuario):
        mejor_coincidencia = None
        mejor_similitud = 0.0
        #Creacion de un bucle que recorre todas las preguntas y respuestas predeterminadas
        for respuesta, preguntas in self.afirmaciones.items():
            # Compara la pregunta usuario utilizando la palabra preguntas [] = pregunta
            for pregunta in preguntas:
                #Utilizando un comando de la librerio difflib comparamos pregunta[n] con la pregunta_usuario
                similitud = difflib.SequenceMatcher(None, pregunta_usuario, pregunta).ratio()
                #Evaluamos la similitud
                if similitud > mejor_similitud:
                    mejor_similitud = similitud
                    mejor_coincidencia = respuesta
         #Ponemos un minimo del 60% para comprobar similitud

        if mejor_coincidencia and mejor_similitud >= 0.6:  # Umbral de similitud
            return mejor_coincidencia
                  



    

        