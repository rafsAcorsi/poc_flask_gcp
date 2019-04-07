"""System config."""
import pathlib
from os import getenv

basedir = pathlib.Path(__file__).resolve().parent


class Config:
    SECRET_KEY = getenv('SECRET_KEY', 'debug')
    DEBUG = False
    URL_BASE = 'localhost'
    SWAGGER_UI = True


class DevelopmentConfig(Config):
    DEBUG = True
    AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    DB_NAME = ''
    PROJECT_ID = ''
    INSTANCE_NAME = ''
    DB_USER = ''
    DB_PASS = ''
    SQLALCHEMY_DATABASE_URI = (
        f'mysql+mysqldb://{DB_USER}:{DB_PASS}@/{DB_NAME}?unix_socket='
        f'/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}'
    )
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = 1800
    SQLALCHEMY_MAX_OVERFLOW = 2


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
