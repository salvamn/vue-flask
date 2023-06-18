from flask import Flask
from flask import request
from flask import jsonify

from flask_cors import CORS

from flask_bcrypt import Bcrypt # https://flask-bcrypt.readthedocs.io/en/1.0.1/

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from config import Config

import os
import json

# Creamos las instancias
app = Flask(__name__)
app.config.from_object(obj=Config)
CORS(app=app, resources={r"/*": {"origins": "*"}})
bcrypt = Bcrypt(app=app)


# Configuramos Firebase

credenciales = credentials.Certificate(cert=Config.CREDENCIAL_FIREBASE)
firebase_admin.initialize_app(credenciales, {
    'databaseURL': 'https://noname-c5a2b-default-rtdb.firebaseio.com/'
})

# Obtenermos una referencia de la base de datos
# Docs de firebase_admin.db: https://firebase.google.com/static/docs/reference/admin/python/firebase_admin.db
# https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/
# https://firebase.google.com/docs/database/admin/start?hl=es-419
referencia = db.reference('/usuario')


#================================================================================================
# Peticiones

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario() -> dict:
    """Este `endpoint` permite la creacion de un usuario mediante un peticion http `post`, recibe un `json` con cuatro propiedades.
    
    nombre -- description\n
    correo -- description\n
    nombre_usuario -- description\n
    contrasenia -- description\n
    
    Return: json con su respuesta.
    """
        
    if request.method == 'POST':
        datos = request.get_json()

        nombre = datos['nombre']
        correo = datos['correo']
        nombre_usuario = datos['nombre_usuario']
        contrasenia = datos['contrasenia']
                
        from models import Usuario
        
        nuevo_usuario = Usuario(nombre=nombre, correo=correo, nombre_usuario=nombre_usuario, contrasenia=bcrypt.generate_password_hash(contrasenia).decode('utf-8'))
                
        try:            
            referencia.push(nuevo_usuario.serializar_json())
            respuesta = f'Nuevo usuario creado: {nombre}'
            
            return jsonify({'respuesta': respuesta})
            
        except Exception as e:
            print(f'error: {e}')
            respuesta = str(e)
            return jsonify({'respuesta': respuesta})
    
        
    
    respuesta = 'Peticion invalida.'
    return jsonify({'respuesta': respuesta})
    


@app.route('/login', methods=['POST'])
def login() -> dict:
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """

    if request.method == 'POST':
        datos = request.get_json()
        
        nombre_usuario = datos['nombre_usuario']
        contrasenia = datos['contrasenia']
        
        print(nombre_usuario, contrasenia)


        usuario = referencia.get()
        
        for key, value in usuario.items():

            if value['nombre_usuario'] == nombre_usuario and bcrypt.check_password_hash(value['contrasenia'], contrasenia):
                return {
                    'nombre': value['nombre'],
                    'nombre_usuario': value['nombre_usuario'],
                    'fecha_registro': value['fecha_registro'],
                    'correo': value['correo'],
                    'is_admin': value['is_admin']
                }

    return {'error': False}





















@app.route('/crear_tarea', methods=['POST'])
def crear_tarea():
    if request.method == 'POST':
        datos = request.get_json()
        
        titulo = datos['titulo']
        correo = datos['correo']
        nombre_usuario = datos['nombre_usuario']
        
        from models import Tarea
        
        tarea = Tarea()











if __name__ == '__main__':
    app.run(debug=True)