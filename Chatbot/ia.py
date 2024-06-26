import openai

# Configura tu clave API de OpenAI


class IAConsultas:
    def obtener_respuesta(self, pregunta):
        # Parámetros de respuesta
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',  # Utiliza el modelo correcto
            messages=[
                {'role': 'system', 'content': "Eres un asistente útil ."},
                {'role': 'user', 'content': pregunta}
            ]
        )

        respuesta = response['choices'][0]['message']['content'].strip()
        return respuesta



# Llamar al método obtener_respuesta con una pregunta




