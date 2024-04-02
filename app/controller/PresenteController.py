from app.httpResponse.HttpResponse import HttpResonse
from app.configurations.DataBase import DB
from app.models.Presente import Presente
from flask_login import login_required
from flask import request


class PresenteController(HttpResonse):

    def renderAdicionarPresente(self):
        return self.responseRender("adicionarPresente.html")
    

    def adicionarPresente(self):
        imagem = request.files['img']
        form = request.form
        listaLinks = [] 
        for x in range(int(form["qtdeLinks"])):
            listaLinks.append(form[f"link_{x}"])

        dictLinks = {
            "links": listaLinks
        }
        presente =  Presente(titulo=form["titulo"], imagem=imagem.read(), nome=imagem.filename, mimType=imagem.mimetype, links=dictLinks)
        presente.converteBytesLinks()

        DB.session.add(presente)
        DB.session.commit()
        return self.responseRedirect(url="presenteBlue.renderAdicionarPresente", mensagem="Presente incluido na lista com sucesso!", categoria="success")
