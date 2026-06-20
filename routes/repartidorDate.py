from datetime import datetime

from models.envio import Envio
from models.repartidor import Repartidor
from routes.envios import join_consulta


def convertir_fecha(fecha):
    return datetime.strptime(fecha, "%Y-%m-%d").date()

def filtrar_fechas(fecha_inicio=None, fecha_fin=None):
    condiciones_envio = [Envio.id_repartidor == Repartidor.id_repartidor]

    if fecha_inicio:
        fecha_inicio_date = convertir_fecha(fecha_inicio)
        condiciones_envio.append(Envio.fecha_envio >= fecha_inicio_date)

    if fecha_fin:
        fecha_fin_date = convertir_fecha(fecha_fin)
        condiciones_envio.append(Envio.fecha_envio <= fecha_fin_date)

    consulta = join_consulta(condiciones_envio)

    return (
        consulta.group_by(
            Repartidor.id_repartidor,
            Repartidor.nombre_Repartidor,
            Repartidor.email,
        )
        .order_by(Repartidor.nombre_Repartidor.asc())
        .all()
    )
