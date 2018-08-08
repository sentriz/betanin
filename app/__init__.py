import os
from flask import Flask

from app.api import api_rest
from app.api import api_bp
from app.client import client_bp

app = Flask(__name__)
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)

from . import config
app.logger.info('>>> {}'.format(config.flask_config))
