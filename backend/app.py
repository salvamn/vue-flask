from flask import Flask
from flask import request
from flask import jsonify

from flask_cors import CORS

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import os

# Creamos las instancias
app = Flask(__name__)
CORS(app=app)


# Configuramos Firebase
ruta_absoluta_certificado = os.path.join(os.getcwd(), 'private', 'noname-c5a2b-firebase-adminsdk-6ewv6-761782c88f.json')
credenciales = credentials.Certificate(cert=ruta_absoluta_certificado)
firebase_admin.initialize_app(credenciales, {
    'databaseURL': 'https://noname-c5a2b-default-rtdb.firebaseio.com/'
})

# Obtenermos una referecia de la base de datos
referencia = db.reference('/usuario')


#================================================================================================
# Peticiones

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    respuesta = None
    
    if request.method == 'POST':
        pass
    
    respuesta = 'Peticion invalida.'
    return respuesta
    


if __name__ == '__main__':
    app.run(debug=True)