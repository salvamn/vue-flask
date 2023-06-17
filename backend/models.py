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
        
    def __repr__(self) -> str:
        return self.nombre_usuario
    
    def serializar_json(self):
        return {'id': self.id, 'nombre': self.nombre, 'correo': self.correo, 'nombre_usuario': self.nombre_usuario, 'contrasenia': self.contrasenia, 'fecha_registro': self.fecha_registro, 'is_admin': str(self.is_admin)}
        
        
class Tarea:
    id: int
    titulo: str
    descripcion: str
    estado: bool
    prioridad: str # baja - media - alta
    fecha_creacion_todo: str
    
    nombre_usuario: str
    
    def __init__(self, titulo, descripcion, prioridad, nombre_usuario, id=None) -> None:
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = True
        self.prioridad = prioridad
        self.fecha_creacion_todo = date.today().strftime("%d/%m/%Y")
        self.nombre_usuario = nombre_usuario
        
    def __repr__(self) -> str:
        return self.titulo
    
    def serializar_json(self):
        return {'id': self.id, 'titulo': self.titulo, 'descripcion': self.descripcion, 'estado': self.estado, 'prioridad': self.prioridad, 'fecha_creacion_todo': self.fecha_creacion_todo, 'nombre_usuario': self.nombre_usuario}
        
    
    


    