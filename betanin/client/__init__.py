import os
from flask import Blueprint, render_template


blueprint = Blueprint(
    'client_app',
    __name__,
    url_prefix='',
    static_url_path='',
    static_folder='./dist',
    template_folder='./dist',
)


@blueprint.route('/')
def index():
    return render_template('index.html')
