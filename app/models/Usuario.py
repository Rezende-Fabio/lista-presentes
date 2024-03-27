from sqlalchemy import Integer, String, Column
from app.configurations.DataBase import DB
from flask_login import UserMixin


class Usuario(UserMixin, DB.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    u_usuario = Column(String(10))
    u_senha = Column(String(65))