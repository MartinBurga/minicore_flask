# Mini-core Flask - Gestion de envios

Aplicacion web desarrollada con Flask y SQLAlchemy para consultar envios registrados por repartidor. La pantalla principal muestra cantidad de envios, total de kilogramos, zona, tarifa aplicada y costo total. Tambien permite filtrar los resultados por rango de fechas.

## Tecnologias

- Python
- Flask
- Flask-SQLAlchemy
- MySQL / PyMySQL
- Jinja2
- Vercel

## Estructura del proyecto

```text
.
|-- app.py                  # Aplicacion Flask principal
|-- index.py                # Crea tablas y puede ejecutar la app localmente
|-- datasql.py              # Inserta datos iniciales de prueba
|-- vercel.json             # Configuracion de rutas para Vercel
|-- models/
|   |-- envio.py            # Modelo Envio
|   |-- repartidor.py       # Modelo Repartidor
|   `-- zona.py             # Modelo Zona
|-- routes/
|   |-- envios.py           # Consulta base de envios
|   `-- repartidorDate.py   # Filtro por fechas
|-- templates/
|   |-- header.html
|   `-- index.html
|-- static/
|   `-- styles.css
`-- utils/
    `-- db.py               # Instancia de SQLAlchemy
```

## Instalacion

1. Crea y activa un entorno virtual:

```bash
python -m venv venv
```

En Windows:

```bash
venv\Scripts\activate
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Configurar el archivo `.env` con la conexion a la base de datos.

4. r las tablas:

```bash
python index.py
```

5. Inserta datos de prueba:

```bash
python datasql.py
```

6. Ejecuta la aplicacion:

```bash
python app.py
```

Luego abre:

```text
http://127.0.0.1:5000
```

## Uso

La pagina principal muestra un resumen agrupado por repartidor. Puedes usar los campos `Fecha inicio` y `Fecha fin` para filtrar los envios por rango de fechas.

## Modelos principales

- `Repartidor`: almacena nombre y correo del repartidor.
- `Zona`: almacena nombre de zona y tarifa por kilogramo.
- `Envio`: almacena peso, fecha, repartidor asignado y zona.

## Despliegue en Vercel

El proyecto incluye `vercel.json`, que redirige las rutas hacia `app.py` y sirve archivos estaticos desde `/static`.

Antes de desplegar, configura en Vercel las variables:

- `DATABASE_URL`
- `SECRET_KEY`

## Notas

- `.env`, entornos virtuales, cache de Python y archivos temporales estan excluidos en `.gitignore`.
- `datasql.py` solo inserta datos si las tablas estan vacias.

## Link a video demostrativo:
https://youtu.be/cCAUjSw-Yzo
