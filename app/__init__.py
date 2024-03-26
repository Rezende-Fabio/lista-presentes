from .configurations import Blueprint
from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    Blueprint.registerBlueprints(app)

    return app