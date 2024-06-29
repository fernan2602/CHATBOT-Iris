import openai

# Configura tu clave API de OpenAI
openai.api_key = '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'

class IAConsultas:
    def obtener_respuesta(self, pregunta):
        # Parámetros de respuesta
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',  # Utiliza el modelo correcto
            messages=[
                {'role': 'system', 'content': "Eres un asistente útil y específico."},
                {'role': 'user', 'content': pregunta}
            ]
        )

        respuesta = response['choices'][0]['message']['content'].strip()
        return respuesta

# Crear una instancia de la clase IAConsultas
consultas = IAConsultas()

# Llamar al método obtener_respuesta con una pregunta
dato = consultas.obtener_respuesta("¿Qué es masturbarse?")
print(dato)



