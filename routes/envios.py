from sqlalchemy import and_, case

from models.envio import Envio
from models.repartidor import Repartidor
from models.zona import Zona
from utils.db import db


def join_consulta(condiciones_envio):
    cantidad_zonas = db.func.count(db.distinct(Zona.id_zona))

    return (
        db.session.query(
            db.func.count(Envio.id_envio).label("cantidad_envios"),
            db.func.coalesce(db.func.sum(Envio.peso_kg), 0).label("total_peso_kg"),
            db.func.coalesce(db.func.sum(Envio.peso_kg * Zona.tarifa_por_kg), 0).label("costo_total"),
            db.func.max(Zona.nombre_zona).label("zona"),
            case(
                (db.func.count(Envio.id_envio) == 0, None),
                (cantidad_zonas == 1, db.func.max(Zona.tarifa_por_kg)),
                else_=None,
            ).label("tarifa_por_kg"),
            Repartidor,
        )
        .outerjoin(Envio, and_(*condiciones_envio))
        .outerjoin(Zona, Envio.id_zona == Zona.id_zona)
    )
