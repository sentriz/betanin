from apscheduler.schedulers.gevent import GeventScheduler
from flask_apscheduler import APScheduler
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restplus import Api
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


cors = CORS()
db = SQLAlchemy(session_options={
    'autocommit': True,
    'autoflush': True,

})
migrate = Migrate()
rest = Api()
scheduler = APScheduler(
    GeventScheduler()
)
socketio = SocketIO(
    # engineio_logger=True,
    # logger=True,
    async_mode='gevent',
)
