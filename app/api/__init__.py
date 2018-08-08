import os
from flask import Flask, Blueprint, session, current_app
from flask_restplus import Api

from app.api import beet_queue
from app.api import torrent_scheduler


api_bp = Blueprint('api_bp',
                   __name__,
                   template_folder='templates',
                   url_prefix='/api')
api_rest = Api(api_bp)


@api_bp.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    # required for webpack dev application to make requests to flask api
    # from another host (localhost:8080)
    if not current_app.config['PRODUCTION']:
        response.headers['Access-Control-Allow-Origin'] = '*'
    return response


from app.api.rest import namespaces
from app.api.rest import resources


beet_queue.start_worker()
torrent_scheduler.start_worker()
