"""Config file for project."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'this-really-needs-to-be-changed'
    DB_URI = "mongodb://localhost"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DB_NAME = "gpsat"
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SERVER_NAME = "localhost:5000"
    DB_NAME = "gpsat_test"


class ProductionConfig(Config):
    DB_NAME = "gpsat"
    DEBUG = False


config = {'development': DevelopmentConfig,
          'testing': TestingConfig,
          'production': ProductionConfig,
          'default': DevelopmentConfig
          }
