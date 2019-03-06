# 3rd party
from flask import Blueprint
from flask import render_template

# betanin
from betanin import paths


api = Blueprint(
    'api_blueprint',
    __name__,
    template_folder='templates',
    url_prefix='/api'
)


client = Blueprint(
    'client_blueprint',
    __name__,
    url_prefix='',
    static_url_path='',
    static_folder=paths.CLIENT_DIST_DIR,
    template_folder=paths.CLIENT_DIST_DIR,
)


@client.route('/')
def index():
    return render_template('index.html')
