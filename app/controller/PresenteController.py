from app.httpResponse.HttpResponse import HttpResonse
from flask_login import login_required
from flask import request


class PresenteController(HttpResonse):

    def renderAdicionarPresente(self):
        return self.responseRender("adicionarPresente.html")
