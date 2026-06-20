from datetime import date
from app import app
from utils.db import db

from models.repartidor import Repartidor
from models.zona import Zona
from models.envio import Envio


class datasql:
    @staticmethod
    def insertar():
        db.create_all()

        if Repartidor.query.count() == 0:
            repartidores = [
                Repartidor(nombre_Repartidor="Martin Burga",  email="martin.burga@gmail.com"), 
                Repartidor(nombre_Repartidor="Carla Castro",  email="carlacastro@gmail.com"),    
                Repartidor(nombre_Repartidor="Sara Gahona",     email="sary@hotmail.com"),   
                Repartidor(nombre_Repartidor="Sergio Ruiz",     email="sergiopro@gmail.com"),   
            ]
            db.session.add_all(repartidores)
            db.session.commit()

        if Zona.query.count() == 0:
            zonas = [
                Zona(nombre_zona="Norte",  tarifa_por_kg=1.50),  
                Zona(nombre_zona="Sur",    tarifa_por_kg=1.25),  
                Zona(nombre_zona="Centro", tarifa_por_kg=1.75),  
            ]
            db.session.add_all(zonas)
            db.session.commit()

        if Envio.query.count() == 0:
            envios = [
                Envio(peso_kg=10.50, fecha_envio=date(2026, 6, 21), id_repartidor=1, id_zona=1),
                Envio(peso_kg=8.00,  fecha_envio=date(2026, 6, 28), id_repartidor=1, id_zona=1),
                Envio(peso_kg=6.30,  fecha_envio=date(2026, 6, 4),  id_repartidor=1, id_zona=1),
                
                Envio(peso_kg=5.25,  fecha_envio=date(2026, 6, 22), id_repartidor=2, id_zona=2),
                Envio(peso_kg=9.00,  fecha_envio=date(2026, 6, 29), id_repartidor=2, id_zona=2),
                Envio(peso_kg=4.75,  fecha_envio=date(2026, 6, 5),  id_repartidor=2, id_zona=2),

                Envio(peso_kg=12.00, fecha_envio=date(2026, 6, 23), id_repartidor=3, id_zona=3),
                Envio(peso_kg=7.50,  fecha_envio=date(2026, 6, 30), id_repartidor=3, id_zona=3),
                Envio(peso_kg=3.80,  fecha_envio=date(2026, 6, 6),  id_repartidor=3, id_zona=3),
            ]
            db.session.add_all(envios)
            db.session.commit()


with app.app_context():
    datasql.insertar()
    print("Datos insertados en bdd.")
