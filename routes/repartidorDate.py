from datetime import datetime

from models.envio import Envio
from models.repartidor import Repartidor
from models.zona import Zona
from utils.db import db


def convertir_fecha(fecha):
    return datetime.strptime(fecha, "%Y-%m-%d").date()


def filtrar_fechas(fecha_inicio=None, fecha_fin=None):
    consulta = (
        db.session.query(Envio, Repartidor, Zona)
        .join(Repartidor, Envio.id_repartidor == Repartidor.id_repartidor)
        .join(Zona, Envio.id_zona == Zona.id_zona)
        .order_by(Envio.fecha_envio.asc())
    )

    if fecha_inicio:
        fecha_inicio_date = convertir_fecha(fecha_inicio)
        consulta = consulta.filter(Envio.fecha_envio >= fecha_inicio_date)

    if fecha_fin:
        fecha_fin_date = convertir_fecha(fecha_fin)
        consulta = consulta.filter(Envio.fecha_envio <= fecha_fin_date)

    return consulta.all()
    

def total_Repartidor(id_repartidor, fecha_inicio=None, fecha_fin=None):
    consulta = (
        db.session.query(
            db.func.coalesce(db.func.sum(Envio.peso_kg * Zona.tarifa_por_kg), 0)
        )
        .join(Zona, Envio.id_zona == Zona.id_zona)
        .filter(Envio.id_repartidor == id_repartidor)
    )

    if fecha_inicio:
        fecha_inicio_date = convertir_fecha(fecha_inicio)
        consulta = consulta.filter(Envio.fecha_envio >= fecha_inicio_date)

    if fecha_fin:
        fecha_fin_date = convertir_fecha(fecha_fin)
        consulta = consulta.filter(Envio.fecha_envio <= fecha_fin_date)

    return consulta.scalar()
