from utils.db import db

class Zona(db.Model):
    __tablename__ = 'zona'
    
    id_zona = db.Column(db.Integer, primary_key=True)
    nombre_zona = db.Column(db.String(50), nullable=False)
    tarifa_por_kg = db.Column(db.Numeric(10,2), nullable=False)
    
    def __init__(self, nombre_zona, tarifa_por_kg):
        self.nombre_zona = nombre_zona
        self.tarifa_por_kg = tarifa_por_kg