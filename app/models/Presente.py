from sqlalchemy import Column, LargeBinary, Integer, String, Text
from app.configurations.DataBase import DB


class Presente(DB.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    p_titulo = Column(String(100))
    p_imagem = Column(Text)
    p_name = Column(Text)
    p_mimeType = Column(Text)
    p_links = Column(LargeBinary)