from .configurations import Blueprint
from .configurations import DataBase
from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "1s2a121#ddwg%$Gfhghfd25w54e&dkd25w"

    DataBase.init_app(app)
    Blueprint.registerBlueprints(app)

    return app