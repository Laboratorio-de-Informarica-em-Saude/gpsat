from config import config
from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    from .api import main_blueprint
    app.register_blueprint(main_blueprint)
    CORS(app, resources=r'/api/*', allow_headers='Content-Type')
    return app


def get_connection(config_name):
    client = MongoClient(config[config_name].DB_URI)
    return client


def get_db(config_name, connection):
    db = connection[config[config_name].DB_NAME]
    return db


def get_db_connection(config_name):
    return get_db(config_name, get_connection(config_name))
