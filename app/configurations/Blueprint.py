

def registerBlueprints(app):
    from app.routes.IndexRoute import indexBlue
    app.register_blueprint(indexBlue)