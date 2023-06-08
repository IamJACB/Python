import requests

# Función para hacer una solicitud a la API de ChatGPT
def obtener_respuesta_chatgpt(pregunta):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': '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'  # Reemplaza "tu_token_de_acceso" con tu propio token de acceso
    }
    data = {
        'messages': [{'role': 'system', 'content': 'Instrucciones para el modelo'}, {'role': 'user', 'content': pregunta}]
    }

    response = requests.post(url, headers=headers, json=data)
    respuesta = response.json()
    return respuesta['choices'][0]['message']['content']

    # Función para interactuar con el usuario
def interactuar_chatgpt():
    print('Bienvenido al ChatGPT!')
    while True:
        pregunta = input('Usuario: ')
        respuesta = obtener_respuesta_chatgpt(pregunta)
        print('ChatGPT:', respuesta)

        # Condiciones para salir del chat
        if pregunta.lower() == 'adios':
            print('ChatGPT: Hasta luego. ¡Que tengas un buen día!')
            break

# Llamada a la función principal de interacción
interactuar_chatgpt()