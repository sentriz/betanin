from betanin import paths


class BaseConfig(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{paths.DB_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "SAMufsdf"


from betanin.config.flask.development import DevelopmentConfig
from betanin.config.flask.production import ProductionConfig


_default = DevelopmentConfig
_config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}


def config_from_string(string):
    search_string = string.lower()
    return _config_map.get(search_string, _default)
