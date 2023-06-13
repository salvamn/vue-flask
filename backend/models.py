from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from datetime import date



# Modelos de las tablas de la db

class Usuario:
    id: int
    nombre: str 
    correo: str
    nombre_usuario: str
    contrasenia: str
    fecha_registro: str
    is_admin: bool
    
    def __init__(self, nombre, correo, nombre_usuario, contrasenia, is_admin=False, id=None) -> None:
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.nombre_usuario = nombre_usuario
        self.contrasenia = generate_password_hash(password=contrasenia)
        self.fecha_registro = date.today().strftime("%d/%m/%Y")
        self.is_admin = is_admin
        
    
    def serializar_json(self):
        return {'id': self.id, 'nombre': self.nombre, 'correo': self.correo, 'nombre_usuario': self.nombre_usuario, 'contrasenia': self.contrasenia, 'fecha_registro': self.fecha_registro, 'is_admin': str(self.is_admin)}
        
        

        
    


    