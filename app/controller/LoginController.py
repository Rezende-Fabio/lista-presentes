from flask_login import login_user, logout_user, login_required
from app.httpResponse.HttpResponse import HttpResonse
from app.models.Usuario import Usuario
from flask import request


class LoginController(HttpResonse):

    def renderLogin(self):
        return self.responseRender("login.html")
    

    def login(self):
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        user = Usuario.query.filter(Usuario.u_usuario==usuario.upper().strip()).first()

        if user:
            if user.verificarSenha(senha):
                login_user(user)
                return self.responseRedirect("loginBlue.renderIndex", mensagem="Login Correto!", categoria="danger")
            
            else:
                return self.responseRedirect("loginBlue.renderIndex", mensagem="Senha incorreta!", categoria="danger")
        else:
            return self.responseRedirect("loginBlue.renderIndex", mensagem="Usuário não existe!", categoria="danger")