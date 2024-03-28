from app.controller.PresenteController import PresenteController
from flask import Blueprint

presenteBlue = Blueprint("presenteBlue", __name__)
presenteController = PresenteController()

presenteBlue.add_url_rule("/adicionar-presente", "renderAdicionarPresente", presenteController.renderAdicionarPresente, methods=["GET"])