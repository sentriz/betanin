from betanin.config import BaseConfig


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True
    PRODUCTION = False
