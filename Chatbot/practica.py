# chatbot.py
import difflib

import 

class Practica:
    def __init__(self):
        self.base_conocimiento =  {
    "Estoy bien, gracias por preguntar.": ["¿Cómo estás?", "¿Qué tal estás?", "¿Cómo te encuentras?"],
    "Es la hora de la verdad.": ["¿Qué hora es?", "¿Hora?", "¿Hora actual?"],
    "Hace sol hoy.": ["¿Qué tiempo hace hoy?", "¿Cómo está el clima hoy?", "¿Qué clima tenemos hoy?"],
    "Me llamo ChatBot.": ["¿Cómo te llamas?", "¿Cuál es tu nombre?", "¿Cómo te denominas?"]
}

    def buscar_pregunta_similar(self, pregunta_usuario):
        mejor_coincidencia = None
        mejor_similitud = 0.0

        for respuesta, preguntas in self.base_conocimiento.items():
            for pregunta in preguntas:
                similitud = difflib.SequenceMatcher(None, pregunta_usuario, pregunta).ratio()
                if similitud > mejor_similitud:
                    mejor_similitud = similitud
                    mejor_coincidencia = respuesta

        if mejor_coincidencia and mejor_similitud >= 0.6:
            return mejor_coincidencia
        else:
            return "Lo siento, no entiendo tu pregunta."



