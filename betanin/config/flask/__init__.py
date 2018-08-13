class Base(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{paths.DB_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


from betanin.config.flask.development import Development
from betanin.config.flask.production import Production


_default = Development
_config_map = {
    'development': Development,
    'production': Production,
}


def config_from_string(string):
    search_string = string.lower()
    return _config_map.get(search_string, _default)
