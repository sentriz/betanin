from betanin.config.flask import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    PRODUCTION = False
