from betanin.config.flask import Base


class Development(Base):
    DEBUG = True
    PRODUCTION = False
