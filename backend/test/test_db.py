import requests # Docs de requests: https://requests.readthedocs.io/en/latest/
import json

url_registro = 'http://127.0.0.1:5000/crear_usuario'
url_login = 'http://127.0.0.1:5000/login'

def test_crear_usuario():
    # Enviar una solicitud POST al servidor
    try:
        response = requests.post(url=url_registro, data={'nombre':'John','correo':'john@example.com','nombre_usuario':'johndoe','contrasenia':'secreta'})
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



def validar_usuario():
    try:
        response = requests.post(url_login, data={'nombre_usuario':'salvamn', 'contrasenia':'12345'})
        print(response)
        
    except Exception as e:
        print(e) 
    
    if response.status_code == 200:
        print('usuario')
        
    else:
        print('ocurrio un error', response.text)



def test_crear_todo():
    pass



test_crear_usuario()
validar_usuario()
