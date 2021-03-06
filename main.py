#!/usr/bin/env python3
from os import getenv

import connexion
import yaml
from connexion import RestyResolver
from flask_sqlalchemy import SQLAlchemy
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

from config import config_by_name

db = SQLAlchemy()


def create_app():
    app = connexion.App(__name__, specification_dir='swagger/')
    app.app.config.from_object(config_by_name[getenv('ENV', 'dev')])
    env = Environment(loader=FileSystemLoader('swagger/'))
    swagger_string = env.get_template('main.yaml').render()
    specification = yaml.safe_load(swagger_string)
    app.add_api(
        specification,
        resolver=RestyResolver('api'),
        options={"swagger_ui": app.app.config.get("SWAGGER_UI")}
    )
    application = app.app
    db.init_app(application)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(
        port=8080, server='gevent', debug=app.app.config['DEBUG']
    )
