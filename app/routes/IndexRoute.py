from app.controller.IndexController import IndexController
from flask import Blueprint

indexBlue = Blueprint("indexBlue", __name__)
indexController = IndexController()

indexBlue.add_url_rule("/index", "renderIndex", indexController.renderIndex, methods=["GET"])
indexBlue.add_url_rule("/", "renderIndexBarra", indexController.renderIndex, methods=["GET"])