from flask import Flask
from flask import request
from flask import jsonify

from flask_cors import CORS

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import os
import json

# Creamos las instancias
app = Flask(__name__)
CORS(app=app, resources={r"/*": {"origins": "*"}})


# Configuramos Firebase
ruta_absoluta_certificado = os.path.join(os.getcwd(), 'private', 'noname-c5a2b-firebase-adminsdk-6ewv6-761782c88f.json')
credenciales = credentials.Certificate(cert=ruta_absoluta_certificado)
firebase_admin.initialize_app(credenciales, {
    'databaseURL': 'https://noname-c5a2b-default-rtdb.firebaseio.com/'
})

# Obtenermos una referencia de la base de datos
referencia = db.reference('/usuario')


#================================================================================================
# Peticiones

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    respuesta = None
    
    if request.method == 'POST':
        datos = request.get_json()

        nombre = datos['nombre']
        correo = datos['correo']
        nombre_usuario = datos['nombre_usuario']
        contrasenia = datos['contrasenia']
                
        from models import Usuario
        
        nuevo_usuario = Usuario(
            nombre=nombre,
            correo=correo,
            nombre_usuario=nombre_usuario,
            contrasenia=contrasenia,
        )
                
        try:            
            referencia.push(nuevo_usuario.serializar_json())
            respuesta = f'Nuevo usuario creado: {nombre}'
            
            return jsonify({'respuesta': respuesta})
            
        except Exception as e:
            print(e)
            respuesta = str(e)
            return jsonify({'respuesta': respuesta})
    
        
    
    respuesta = 'Peticion invalida.'
    return jsonify({'respuesta': respuesta})
    


if __name__ == '__main__':
    app.run(debug=True)