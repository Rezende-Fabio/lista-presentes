from app.httpResponse.HttpResponse import HttpResonse
from app.models.Presente import Presente
import base64

class IndexController(HttpResonse):

    def renderIndex(self):
        presentes = Presente.query.all()
        listaPresentes = []
        for presente in presentes:
            listaPresentes.append({"id": presente.id, "titulo": presente.p_titulo, "imagem": base64.b64encode(presente.p_imagem).decode('utf-8')})

        context = {"presentes": listaPresentes}
        return self.responseRender("index.html", context=context)