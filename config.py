# config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Configuración para MySQL
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/bdFlask'
SQLALCHEMY_TRACK_MODIFICATIONS = False


