import betanin
from betanin.minimal_context import *


betanin.register_blueprints(app)
socketio = betanin.register_socketio(app)
