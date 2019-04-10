# 3rd party
from flask import Blueprint

# betanin
from betanin import paths


API = Blueprint(
    "api_blueprint",
    "api blueprint",
    template_folder="templates",
    url_prefix="/api",
)
CLIENT = Blueprint(
    "client_blueprint",
    "client blueprint",
    url_prefix="",
    static_url_path="",
    static_folder=paths.CLIENT_DIST_DIR,
    template_folder=paths.CLIENT_DIST_DIR,
)
