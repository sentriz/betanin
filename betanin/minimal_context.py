import betanin


app = betanin.init_app()
db = betanin.register_orm(app)


__all__ = ['app', 'db']
