import pymysql, os
from flask import Flask, render_template, request
from utils.db import db
from dotenv import load_dotenv

from models.envio import Envio
from models.repartidor import Repartidor
from models.zona import Zona
from routes.repartidorDate import filtrar_fechas, total_Repartidor
from routes.envios import costoEnvio


load_dotenv()
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY')

db.init_app(app)


@app.route("/")
def home():
    fecha_inicio = request.args.get("fecha_inicio")
    fecha_fin = request.args.get("fecha_fin")
    envios = filtrar_fechas(fecha_inicio, fecha_fin)

    return render_template(
        "index.html",
        envios=envios,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
    )

if __name__ == "__main__":
    app.run(debug=True)
