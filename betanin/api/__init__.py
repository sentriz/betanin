import os

from flask import Blueprint
from flask import Flask
from flask import current_app


blueprint = Blueprint(
    'api_bp',
    __name__,
    template_folder='templates',
    url_prefix='/api'
)


from betanin.api.rest import namespaces
import betanin.api.rest.resources.settings
import betanin.api.rest.resources.torrents
