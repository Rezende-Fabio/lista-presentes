from app.controller.LoginController import LoginController
from flask import Blueprint

loginBlue = Blueprint("loginBlue", __name__)
loginController = LoginController()

loginBlue.add_url_rule("/login", "renderIndex", loginController.renderLogin, methods=["GET"])
loginBlue.add_url_rule("/login", "login", loginController.login, methods=["POST"])
