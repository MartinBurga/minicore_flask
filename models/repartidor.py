from utils.db import db

class Repartidor(db.Model):
    __tablename__ = 'repartidor'
    
    id_repartidor = db.Column(db.Integer, primary_key=True)
    nombre_Repartidor = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    
    
    def __init__(self, nombre_Repartidor, email):
        self.nombre_Repartidor = nombre_Repartidor
        self.email = email