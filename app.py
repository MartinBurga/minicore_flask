from flask import Flask, render_template, Blueprint
from utils.db import db
from dotenv import load_dotenv

from models.envio import Envio
from models.repartidor import Repartidor
from models.zona import Zona

import pymysql, os

load_dotenv()
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY')



@app.route("/")
def home():
    return render_template("index.html")

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
