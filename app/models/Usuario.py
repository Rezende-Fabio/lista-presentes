from sqlalchemy import Integer, String, Column
from app.configurations.DataBase import DB
from flask_login import UserMixin
import bcrypt


class Usuario(UserMixin, DB.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    u_usuario = Column(String(10))
    u_senha = Column(String(65))

    def __init__(self, usuario: str, senha: str) -> None:
        self.u_usuario = usuario
        self.u_senha = senha


    def verificarSenha(self, senha: str) -> bool:
        hash = bcrypt.checkpw(senha.encode('utf-8'), self.u_senha.encode('utf-8'))
        if hash:
            return True
        else:
            return False
        
    