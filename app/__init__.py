from app.configurations import Blueprint
from app.configurations import DataBase
from app.configurations import Auth
from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "1s2a121#ddwg%$Gfhghfd25w54e&dkd25w"

    DataBase.init_app(app)
    Auth.init_app(app)
    Blueprint.registerBlueprints(app)

    return app