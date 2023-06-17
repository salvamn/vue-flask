import requests
import json

url = 'http://127.0.0.1:5000/crear_usuario'

def test_crear_usuario():
    # Enviar una solicitud POST al servidor
    try:
        response = requests.post(url, data={'nombre':'John','correo':'john@example.com','nombre_usuario':'johndoe','contrasenia':'secreta'})
        print(response)
    except Exception as e:
        print(e)
        
    # Verificar la respuesta del servidor
    if response.status_code == 200:
        print("El usuario se creó correctamente.")
    else:
        print("Ocurrió un error al crear el usuario:", response.text)
        # print("Ocurrió un error al crear el usuario:", response.reason)
        
# def test_traer_usuarios():
    
    



def test_crear_todo():
    pass
