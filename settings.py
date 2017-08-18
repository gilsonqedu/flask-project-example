# -*- coding: utf-8 -*-

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 's3cret key'
    MONGODB_SETTINGS = {
        'db': os.environ.get('QEDU_PREASSESSMENT_DB_NAME'),
        'host': os.environ.get('QEDU_PREASSESSMENT_DB_HOST'),
        'port': os.environ.get('QEDU_PREASSESSMENT_DB_PORT'),
        'username': os.environ.get('QEDU_PREASSESSMENT_DB_USERNAME'),
        'password': os.environ.get('QEDU_PREASSESSMENT_DB_PASSWD')
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'qeduprovas',
        'host': 'localhost',
        'port': 27017
    }


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # Logging
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
