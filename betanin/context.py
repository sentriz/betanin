import betanin


# base
app = betanin.init_app()
betanin.register_blueprints(app)

# db
db = betanin.register_orm(app)

# socketio  
socketio = betanin.register_socketio(app)
