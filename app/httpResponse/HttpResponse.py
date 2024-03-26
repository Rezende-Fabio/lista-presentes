from flask import redirect, render_template, Response, flash, url_for
from typing import Optional
import json

class HttpResonse:

    def responseRender(self, arquivo: str, context: Optional[dict]=None) -> render_template:
        if context != None: 
            return render_template(arquivo, context=context)
        
        return render_template(arquivo)


    def responseRedirect(self, url: str, mensagem: Optional[str]=None, categoria: Optional[str]=None) -> redirect:
        if mensagem != None: flash(mensagem, categoria)
        
        return redirect(url_for(url))
    

    def responseJson(self, status: int, body: Optional[dict]=None) -> Response:
        if body:
            response = Response(json.dumps(body), status=status, mimetype="application/json")
        else:
            response = Response(status=status)

        return response