

def registerBlueprints(app):
    from app.routes.IndexRoute import indexBlue
    app.register_blueprint(indexBlue)

    from app.routes.LoginRoute import loginBlue
    app.register_blueprint(loginBlue)