import os

from betanin.config.flask import BaseConfig


class ProductionConfig(BaseConfig):
    DEBUG = False
    PRODUCTION = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'UnsafeSecret')
