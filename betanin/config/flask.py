# betanin
from betanin import paths


SQLALCHEMY_DATABASE_URI = f"sqlite:///{paths.DB_PATH}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
JWT_ACCESS_TOKEN_EXPIRES = 604_800
CORS_ORIGIN_WHITELIST = (
    "http://0.0.0.0:9393",
    "http://0.0.0.0:8081",
    "http://localhost:8080",
    "http://localhost:8080/",
    "http://localhost:9393",
    "http://localhost:8081",
)
