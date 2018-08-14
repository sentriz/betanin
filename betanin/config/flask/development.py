from betanin.config.flask import BaseConfig


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True
    PRODUCTION = False
