from utils.db import db

class Envio(db.Model):
    __tablename__ = 'envio'
    
    id_envio = db.Column(db.Integer, primary_key=True)
    peso_kg = db.Column(db.Numeric(10, 2), nullable=False)
    fecha_envio = db.Column(db.Date, nullable=False)

    # Foreign Keys
    id_repartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id_repartidor'), nullable=False)
    id_zona = db.Column(db.Integer, db.ForeignKey('zona.id_zona'), nullable=False)

    def __init__(self, peso_kg, fecha_envio, id_repartidor, id_zona):
        self.peso_kg = peso_kg
        self.fecha_envio = fecha_envio
        self.id_repartidor = id_repartidor
        self.id_zona = id_zona