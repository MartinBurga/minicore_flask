from flask import Blueprint

envios_bp = Blueprint("envios", __name__)


def costoEnvio(envio, zona):
    costototal = envio.peso_kg * zona.tarifa_por_kg
    return costototal
