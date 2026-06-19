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
                Repartidor(nombre_Repartidor="Carlos Mendoza", email="carlos@email.com"),
                Repartidor(nombre_Repartidor="Ana Torres", email="ana@email.com"),
                Repartidor(nombre_Repartidor="Luis Ramirez", email="luis@email.com"),
                Repartidor(nombre_Repartidor="Maria Lopez", email="maria@email.com"),
            ]

            db.session.add_all(repartidores)
            db.session.commit()

        if Zona.query.count() == 0:
            zonas = [
                Zona(nombre_zona="Norte", tarifa_por_kg=1.50),
                Zona(nombre_zona="Sur", tarifa_por_kg=1.25),
                Zona(nombre_zona="Centro", tarifa_por_kg=1.75),
                Zona(nombre_zona="Valle", tarifa_por_kg=2.00),
            ]

            db.session.add_all(zonas)
            db.session.commit()

        if Envio.query.count() == 0:
            envios = [
                Envio(peso_kg=10.50, fecha_envio=date(2026, 5, 21), id_repartidor=1, id_zona=1),
                Envio(peso_kg=5.25, fecha_envio=date(2026, 5, 22), id_repartidor=2, id_zona=2),
                Envio(peso_kg=8.00, fecha_envio=date(2026, 5, 23), id_repartidor=3, id_zona=3),
                Envio(peso_kg=12.75, fecha_envio=date(2026, 5, 24), id_repartidor=4, id_zona=4),
                Envio(peso_kg=3.50, fecha_envio=date(2026, 5, 25), id_repartidor=1, id_zona=2),
                Envio(peso_kg=7.20, fecha_envio=date(2026, 5, 26), id_repartidor=2, id_zona=3),
                Envio(peso_kg=15.00, fecha_envio=date(2026, 5, 27), id_repartidor=3, id_zona=1),
                Envio(peso_kg=6.80, fecha_envio=date(2026, 5, 28), id_repartidor=4, id_zona=4),
            ]

            db.session.add_all(envios)
            db.session.commit()


with app.app_context():
    datasql.insertar()
    print("Datos insertados en bdd.")