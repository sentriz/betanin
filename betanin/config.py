# betanin
from betanin import paths


class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{paths.DB_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "GUYSILOVEIT"
    CORS_ORIGIN_WHITELIST = [
        'http://0.0.0.0:5000',
        'http://localhost:5000',
        'http://0.0.0.0:8081',
        'http://localhost:8081',
    ]
