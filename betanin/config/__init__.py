from betanin import paths

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


_sql_url = f'sqlite:///{paths.DB_PATH}'


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = _sql_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "GUYSILOVEIT"
    CORS_ORIGIN_WHITELIST = [
        'http://0.0.0.0:5000',
        'http://localhost:5000',
        'http://0.0.0.0:8081',
        'http://localhost:8081',
    ]
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url=_sql_url)
    }
    SCHEDULER_API_ENABLED = True
    JOBS = [
        {
            'id': 'fetch_torrents',
            'func': 'betanin.api.jobs.fetch_torrents:start',
            'trigger': 'interval',
            'seconds': 2,
            'replace_existing': True,

        },
        {
            'id': 'process_torrents',
            'func': 'betanin.api.jobs.process_torrents:start',
            'replace_existing': True,
            'trigger': 'date',

        },
        {
            'id': 'make_sessions',
            'func': 'betanin.api.jobs.make_sessions:start',
            'replace_existing': True,
            'trigger': 'date',

        }
    ]


from betanin.config.development import DevelopmentConfig
from betanin.config.production import ProductionConfig


_default = DevelopmentConfig
_config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}


def config_from_string(string):
    search_string = string.lower()
    return _config_map.get(search_string, _default)
