from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lista.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)

    with app.app_context():
        from app.models.Usuario import Usuario
        from app.models.Presente import Presente
        DB.create_all()