from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()#recordar que esta usara en toda la aplicacion este caso esta usando el modelo task

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    # Configura la base de datos con la aplicación
    db.init_app(app)

    # Importar los modelos para que SQLAlchemy los conozca
    from app.models.Task import Tarea

    from app.routes.routeTask import tareaRoute
    app.register_blueprint(tareaRoute)

    # Devuelve la aplicación configurada
    return app
