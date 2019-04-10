"""System config."""
import pathlib
from os import getenv

basedir = pathlib.Path(__file__).resolve().parent


class Config:
    SECRET_KEY = getenv('SECRET_KEY', 'debug')
    DEBUG = False
    URL_BASE = 'localhost'
    SWAGGER_UI = True
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL', 'sqlite:///test.db')


class DevelopmentConfig(Config):
    DEBUG = True
    AUTO_RELOAD = True
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = 1800
    SQLALCHEMY_MAX_OVERFLOW = 2


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    PROJECT_ID = getenv('PROJECT_ID')
    INSTANCE_NAME = getenv('INSTANCE_NAME')
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
