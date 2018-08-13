import os

from flask import Blueprint
from flask import Flask
from flask import current_app

from betanin.api import beet_queue
from betanin.api import torrent_scheduler


blueprint = Blueprint(
    'api_bp',
    __name__,
    template_folder='templates',
    url_prefix='/api'
)


from betanin.api.rest import namespaces
from betanin.api.rest import resources


beet_queue.start_worker()
torrent_scheduler.start_worker()
