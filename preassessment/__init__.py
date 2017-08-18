# -*- coding: utf-8 -*-

from flask import Flask

from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow

from settings import config

# Initialize extensions
db = MongoEngine()
marshmallow = Marshmallow()


def create_app(config_name):
    app = Flask('preassessment')
    app.config.from_object(config[config_name])

    # Register extensions
    db.init_app(app)
    marshmallow.init_app(app)

    # Register blueprints
    from .core import core as core_blueprint
    app.register_blueprint(core_blueprint)

    from .students import students as students_blueprint
    app.register_blueprint(students_blueprint)

    return app
